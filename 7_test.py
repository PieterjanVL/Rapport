import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys
import pandas as pd

df = pd.read_csv(os.getcwd() + '/data.csv').drop_duplicates()
print(df)

print(os.path.exists(os.getcwd()))
print('File is gemaakt' + os.getcwd())

print(os.path.exists(os.getcwd() + '/analyse/2022-12-08_18-48-34'))
print('File is gemaakt' + os.getcwd() + '/analyse')

os.makedirs(os.getcwd() + '/analyse/test4')

print(os.path.exists(os.getcwd() + '/analyse/test4'))
print('File is gemaakt' + os.getcwd() + '/analyse/test4')