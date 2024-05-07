from random import randint
import pandas as pd

sorteados = set()
while len(sorteados) < 32:
    sorteados.add(randint(0, 265))

print(len(sorteados))
print(sorteados)

arquivo = 'empresas.xlsx'
planilha = pd.read_excel(arquivo)

empresas_sorteadas = []
for indice, linha in planilha.iterrows():
    if indice in sorteados:
        empresas_sorteadas.append({
            'linha': indice + 2,
            'setor': linha['setor'], 
            'tamanho': linha['tamanho'], 
            'nome': linha['nome'], 
            'funcionarios': linha['funcionarios']
        })

with pd.ExcelWriter(arquivo, engine='openpyxl', mode='a') as writer:
    pd.DataFrame(empresas_sorteadas).to_excel(writer, sheet_name='amostra', index=False)
