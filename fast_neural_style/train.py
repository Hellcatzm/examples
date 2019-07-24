# author: hellcatzm
# data:   2019/7/24

import os
import subprocess

commands = [
    """
    python neural_style/neural_style.py train \
    --dataset '../../DataSet/coco/' \
    --style-image './images/style-images/mosaic.jpg' \
    --save-model-dir './checkpoints' \
    --epochs 2 \
    --cuda 1
    """
]

for cmd in commands:
    print("Process command '{}' ...".format(cmd))
    try:
        p = subprocess.Popen(cmd, shell=True)
        p.wait()
    except RuntimeError as e:
        continue