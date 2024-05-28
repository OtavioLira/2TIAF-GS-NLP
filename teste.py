import nltk
import re
import pandas as pd
import os
from nltk.sentiment import SentimentIntensityAnalyzer

# Carregar arquivos TXT
def carregar_arquivos_txt(pasta):
  """
  Carrega todos os arquivos TXT em uma pasta como uma lista de strings.

  Argumentos:
    pasta: O caminho para a pasta que contém os arquivos TXT.

  Retorna:
    Uma lista de strings contendo o conteúdo dos arquivos TXT.
  """
  arquivos = []
  for arquivo in os.listdir(pasta):
    if arquivo.endswith(".txt"):
      caminho_arquivo = os.path.join(pasta, arquivo)
      with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        texto = f.read()
        arquivos.append(texto)
  return arquivos

# Função para extrair sentimento de um texto
def extrair_sentimento(texto):
  """
  Extrai o sentimento de um texto usando o NLTK.

  Argumentos:
    texto: O texto a ser analisado.

  Retorna:
    Uma tupla contendo o sentimento (positivo, negativo ou neutro) e a pontuação.
  """
  sentimento = nltk.sentiment.vader.SentimentIntensityAnalyzer().polarity_scores(texto)
  if sentimento['pos'] > sentimento['neg']:
    return ('positivo', sentimento['pos'])
  elif sentimento['neg'] > sentimento['pos']:
    return ('negativo', sentimento['neg'])
  else:
    return ('neutro', 0)

# Função para extrair informações de um texto
def extrair_informacoes(texto):
  """
  Extrai informações relevantes de um texto, como local e pessoa envolvida.

  Argumentos:
    texto: O texto a ser analisado.

  Retorna:
    Um dicionário contendo as informações extraídas.
  """
  informacoes = {}

  # Extrair localização usando regex
  localizacao_regex = r"(?:\b[A-Z][a-z]+\b(?:\s[A-Z][a-z]+)*){2,}"
  localizacao = re.findall(localizacao_regex, texto)
  if localizacao:
    informacoes['localizacao'] = localizacao[0]

  # Extrair pessoa envolvida usando regex
  pessoa_regex = r"@\w+"
  pessoa = re.findall(pessoa_regex, texto)
  if pessoa:
    informacoes['pessoa_envolvida'] = pessoa[0]

  return informacoes

# Carregar arquivos TXT
pasta_arquivos = "assets/tweets"
textos = carregar_arquivos_txt(pasta_arquivos)

# Processar textos
dados = []
for texto in textos:
  # Extrair sentimento
  sentimento, pontuacao = extrair_sentimento(texto)

  # Extrair informações
  informacoes = extrair_informacoes(texto)

  # Criar dicionário com dados do texto
  dados_texto = {
    "texto": texto,
    "sentimento": sentimento,
    "pontuacao_sentimento": pontuacao,
    "localizacao": informacoes.get("localizacao"),
    "pessoa_envolvida": informacoes.get("pessoa_envolvida")
  }

  # Adicionar dicionário à lista de dados
  dados.append(dados_texto)

# Converter dados em DataFrame
df_textos = pd.DataFrame(dados)

# Salvar DataFrame em CSV
df_textos.to_csv("analise_poluicao_oceanica.csv", index=False)

# Exibir DataFrame
print(df_textos.head())
