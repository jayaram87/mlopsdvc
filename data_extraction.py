import os
from glob import glob

dirs = ["Training_Batch_Files", "Prediction_Batch_files"]

for i in dirs:
    files = glob(i+r'/*.csv')
    for path in files:
        os.system(f'dvc add {path}')
        print(f'add {path}')