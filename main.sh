#!/bin/bash

python yolo5.py
python crop.py
mkdir -p results_resize_768_1024
python resize_768_1024.py
