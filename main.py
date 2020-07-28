import pandas as pd
import subprocess
import os

path = os.getcwd()
df = pd.read_csv("keyword.csv")  
keywords = df['Country'].tolist()  

processes = []
for keyword in keywords:
    p = subprocess.Popen(["python", "run.py", keyword], cwd=path)
    processes.append(p)
    
for p in processes:
    p.wait()