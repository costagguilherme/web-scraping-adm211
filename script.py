from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pandas as pd
import os
import sys

driver = webdriver.Chrome()
empresas = []

def get_data(uri):
    driver.get(uri['link'])
    driver.implicitly_wait(300)
    nomesEmpresas = driver.find_elements(By.XPATH, "//td[@data-th='Empresa']")
    numFuncionarios  = driver.find_elements(By.XPATH, "//td[@data-th='Funcionários']")

    print(numFuncionarios[0].text)
    for i in range(len(nomesEmpresas)):
        nomeEmpresa = nomesEmpresas[i].text
        numFuncionario = numFuncionarios[i].text
        empresas.append({'setor': uri['setor'], 'tamanho': uri['tamanho'], 'nome': nomeEmpresa, 'funcionarios': numFuncionario})
        print(f'Empresa: {nomeEmpresa}, N° Funcionários: {numFuncionario}')



uris = [
    {
        "setor": "tecnologia",
        "tamanho": "media",
        "link": "https://gptw.com.br/ranking/melhores-empresas-para-trabalhar/?ano=2023&tipo=Setorial&ranking=Tecnologia&corte=M%C3%A9dias", 
    },
    {
        "setor": "tecnologia",
        "tamanho": "grande",
        "link": "https://gptw.com.br/ranking/melhores-empresas-para-trabalhar/?ano=2023&tipo=Setorial&ranking=Tecnologia&corte=Grandes"
    },
    {
        "setor": "agronegocio",
        "tamanho": "media",
        "link": "https://gptw.com.br/ranking/melhores-empresas-para-trabalhar/?ano=2023&tipo=Setorial&ranking=Agronegocio&corte=M%C3%A9dias", 
    },
    {
        "setor": "agronegocio",
        "tamanho": "grande",
        "link": 'https://gptw.com.br/ranking/melhores-empresas-para-trabalhar/?ano=2023&tipo=Setorial&ranking=Agronegocio&corte=Grandes'
    },
    {
        "setor": "industria",
        "tamanho": "media",
        "link": "https://gptw.com.br/ranking/melhores-empresas-para-trabalhar/?ano=2023&tipo=Setorial&ranking=Industria&corte=M%C3%A9dias", 
    },
    {
        "setor": "industria",
        "tamanho": "grande",
        "link": "https://gptw.com.br/ranking/melhores-empresas-para-trabalhar/?ano=2023&tipo=Setorial&ranking=Industria&corte=Grandes"
    },
    {
        "setor": "varejo",
        "tamanho": "media",
        "link": "https://gptw.com.br/ranking/melhores-empresas-para-trabalhar/?ano=2023&tipo=Setorial&ranking=Varejo&corte=M%C3%A9dias", 
    },
    {
        "setor": "varejo",
        "tamanho": "grande",
        "link": 'https://gptw.com.br/ranking/melhores-empresas-para-trabalhar/?ano=2023&tipo=Setorial&ranking=Varejo&corte=Grandes'
    }
]


for uri in uris:
    get_data(uri)
    
    

empresas_unicas = []
empresas_vistas = set()

for empresa in empresas:
    nome_empresa = empresa["nome"]
    if nome_empresa not in empresas_vistas:
        empresas_unicas.append(empresa)
        empresas_vistas.add(empresa['nome'])


driver.quit()

df = pd.DataFrame(empresas_unicas)

# Especificar o caminho e nome do arquivo Excel
file = "./exemplo.xlsx"

# Salvar o DataFrame no arquivo Excel
df.to_excel(file, index=False)
print("***PLANILHA SALVA COM SUCESSO***")
os.system(f"xdg-open {file}")