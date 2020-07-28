import pandas as pd
import os
import subprocess

path = os.getcwd()
keywords = pd.read_csv("keyword.csv")

for i in keywords.index:
    keyword = keywords['Character'][i]
    subprocess.Popen(["python", "run.py", keyword], cwd=path)