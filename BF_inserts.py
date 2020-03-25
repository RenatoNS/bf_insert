# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 11:26:44 2020

@author: renatons
"""
#%%
import pandas as pd
import os
import csv
import gzip
import io
from unicodedata import normalize
import numpy as np
#%%
pasta = r'C:\Users\RenatoNS\Desktop\workspace\BF_inserts'
os.chdir(pasta)

#%%
def encode(name):
    ascii_name = normalize("NFKD", name).encode("ascii", errors="ignore").decode("ascii")
    return ascii_name.upper()


def load_data():
    fobj = io.TextIOWrapper(gzip.open("nomes.csv.gz"), encoding="utf-8")
    csv_reader = csv.DictReader(fobj)
    data = {
        row["first_name"]: row["classification"]
        for row in csv_reader
    }
    fobj.close()
    return data


def classifica(name):
    encoded_name = encode(name)
    try:
      name_data[encoded_name]
    except:
      return np.nan
    else:
      return name_data[encoded_name]
    
      


#%%
df = pd.read_csv('201912_BolsaFamilia_Pagamentos.csv', sep=';', encoding='latin1')

df = df.iloc[:100, :]

df = df.loc[:,'NOME FAVORECIDO']
df = pd.DataFrame(df)
df['GENERO'] = np.nan

#%%
name_data = load_data()
print(f"Dicionário criado com {len(name_data)} nomes.")

generos = []

for nome in df['NOME FAVORECIDO']:
  generos.append(classifica(nome.split()[0]))
  
df['GENERO'] = generos
  
  
  







