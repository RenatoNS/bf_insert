# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:54:02 2020

@author: renatons
"""
#%%
import pandas as pd
import os
import numpy as np
from selenium import webdriver

#%%
pasta = r'C:\Users\RenatoNS\Desktop\workspace\BF_inserts'
os.chdir(pasta)

#%%
df = pd.read_csv('201912_BolsaFamilia_Pagamentos.csv', sep=';', encoding='latin1')

df = df.iloc[:100, :]

df = df[['NOME FAVORECIDO','NIS FAVORECIDO']]

#%%
class ChromeAuto:
    def __init__(self):
        self.driver_path = 'chromedriver'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('user-data-dir=Perfil')
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )
        
        
    def acessa(self, site):
      self.chrome.get(site)
    
    def sair(self):
      self.chrome.quit()
      
    def clica_consulta(self):
      try:
        btn_consulta = self.chrome.find_element_by_css_selector('#cadastro_senha > table > tbody > tr:nth-child(3) > td > a')
        btn_consulta.click()
      except Exception as e:
        print('Erro ao clicar em Consulta benefícios por família', e)
        
        
if __name__ == '__main__':
  chrome = ChromeAuto()

  chrome.acessa('https://www.beneficiossociais.caixa.gov.br/consulta/beneficio/04.01.00-00_00.asp')
  chrome.clica_consulta()
  
  #chrome.sair()