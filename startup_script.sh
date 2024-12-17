#!/bin/bash

source /home/bot/miniconda3/etc/profile.d/conda.sh

conda activate face

cd /home/bot/Desktop/home_guard/

xvfb-run python3 attendance_taker.py >> /home/bot/debug.log 2>&1
