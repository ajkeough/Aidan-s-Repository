#!/usr/bin/env python3

import subprocess
import os
#Origin of the dataset
#https://www.kaggle.com/gpreda/covid-world-vaccination-progress

os.chdir('/Users/aidansstuff/Downloads')


import pandas as pd
df = pd.read_csv(r'/Users/aidansstuff/Downloads/country_vaccinations.csv')
df = df.drop(columns=['source_website', 'source_name', 'iso_code'], axis=1)

df.info()

#change the file type from .CSV to .TSV
csv.writer(open('country_vaccinations.tsv', 'w+'), delimiter='\t').writerows(csv.reader(open("country_vaccinations.csv")))

