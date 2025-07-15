#!/bin/bash

cd /home/yandan/workspace/sd3.5
source .sd3.5/bin/activate
python sd3_infer_acdc.py
deactivate
