import pandas as pd

# Exemplo de DataFrame com informações dos alunos
data = {'Nome': ['João', 'Maria', 'Pedro'],
        'Média': [8.5, 9.3, 7.8]}

df = pd.DataFrame(data)

# Encontrando o aluno com a maior média
indice_aluno_max_media = df['Média'].idxmax()
aluno_max_media = df.loc[indice_aluno_max_media]

# Imprimindo o nome do aluno e sua média
print("Aluno:", aluno_max_media['Nome'])
print("Média:", aluno_max_media['Média'])