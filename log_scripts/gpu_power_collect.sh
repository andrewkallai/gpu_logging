#!/bin/bash

MS_INTERVAL=100

#sbatch --wait gpu_power_batch.qs
sbatch --wait gpu_power_batch.qs ${MS_INTERVAL}
python3.12 plot_power.py ${MS_INTERVAL}
