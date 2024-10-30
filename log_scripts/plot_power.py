from argparse import ArgumentParser
from pandas import read_csv
import matplotlib.pyplot as plt


def create_power_plot(display: bool = False, img_format: str = 'pdf') -> None:
    parser = ArgumentParser(
        description=
        "Process and plot data in a CSV file containing GPU power measurements."
    )
    parser.add_argument('interval',
                        type=int,
                        help="Millisecond interval for power samples.")
    interval = parser.parse_args().interval

    df = read_csv("./nv_smi_out.csv", skipinitialspace=True)
    power_readings = df["power.draw.instant [W]"].to_list()
    power_length = len(power_readings)
    time = list(range(0, power_length * interval, interval))

    plt.plot(time, power_readings, '-o')
    plt.xlabel('Time (Milliseconds)')
    plt.ylabel('Instant Power Draw (Watts)')
    max_y, min_y = max(power_readings), min(power_readings)
    max_x, min_x = time[power_readings.index(max_y)], time[
        power_readings.index(min_y)]
    plt.text(max_x,
             max_y,
             f"({max_x:.2f}, {max_y:.2f})",
             ha="center",
             va="bottom",
             color="red")
    plt.text(min_x,
             min_y,
             f"({min_x:.2f}, {min_y:.2f})",
             ha="center",
             va="top",
             color="red")

    plt.title(
        str(interval) + " ms Spaced GPU Power Measurements during a " +
        str((power_length - 1) * interval) + " ms Period")

    if (display):
        plt.show()
    else:
        plt.savefig(fname=f"power_measurements.{img_format}",
                    format=img_format)
    plt.close()


if __name__ == '__main__':
    create_power_plot()
