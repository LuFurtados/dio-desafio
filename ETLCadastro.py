import pandas as pd
import json as js

#EXTRACT
# Lê o CSV e converte para uma lista de dicionários
users = pd.read_csv('BDCadUser02.csv', sep = ';').to_dict(orient='records')

#TRANSFORMATION
# Garante a estrutura esperada para a etapa de Transformação e indlui novas colunas

for user in users:
    user['Filial'] = []

for user in users:
  user['Filial'].append({
      "Local_Trab": "Rio de Janeiro",
      "Obs": "Transferido de Santa Catarina",
  })

#LOAD
#Transforma o arquivo em um json para importação
print(js.dumps(users, indent=2))