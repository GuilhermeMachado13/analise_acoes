# -*- coding: utf-8 -*-
"""bot_analisar_acoes.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1WrcKUb_lAeH_KTxypZsfgJZ6GRRjJ0NC
"""

import requests
from bs4 import BeautifulSoup
cabecalho={'user-agent': 'Mozilla/5.0'} ## 
sigla_acao=input('Informe a sigla da ação:\n')# entrar com o código da ação
codigo_acao=f'https://statusinvest.com.br/acoes/{sigla_acao}' # 
resposta=requests.get(codigo_acao, headers= cabecalho) # fazendo a requisição para acessar o site
emaranhado=resposta.text                          
emaranhado_legal=BeautifulSoup(emaranhado, 'html.parser')
print('\n')

print(f'---Informações Gerais---')
print('\n')

def nome_acao():  ## função para mostrar o código e o nome da ação requisitado
  acronimo=emaranhado_legal.find_all('h1', class_="lh-4") 
  acao=acronimo[0].text.replace(" ", "")
  print(f'Ação: {acao}')

nome_acao()

def setor_atuacao(): ## função para mostrar o setor de atuação da empresa
  setor=emaranhado_legal.find_all('div', class_="info pr-md-2")
  setor_atuacao=setor[0].find('strong').text
  print(f'Setor de Atuação: {setor_atuacao}')

setor_atuacao()  

def subsetor_atuacao(): ## função para mostrar o subsetor de atuação da empresa
  subsetor=emaranhado_legal.find_all('div', class_="info pl-md-2 pr-md-2")
  subsetor_atuacao=subsetor[0].find('strong').text
  print(f'Subsetor de Atuação: {subsetor_atuacao}')

subsetor_atuacao()

def segmento_atuacao(): ## função para mostrar o segmento de atuação de atuação da empresa
  segmento=emaranhado_legal.find_all('div', class_="info pl-md-2 ")
  segmento_atuacao =segmento[0].find('strong').text
  print(f'Segmento de Atuação: {segmento_atuacao}')

segmento_atuacao()

def valor_acao(): ## função para mostrar o valor da cotaçãoda empresa
  valor_atual=emaranhado_legal.find_all('strong', class_="value")
  valor_atual[0].text
  print(f'Valor da Cotação: R$ {float(valor_atual[0].text.replace(",", "."))}')

valor_acao()  

def valorizacao_acao(): ## função para mostrar a valorização da empresa em 1 ano
  valorizacao=emaranhado_legal.find_all('div', class_="info w-50 w-md-50 w-lg-20")
  valorizacao_acao=valorizacao[0].find('strong').text.replace("%", "").replace(",", ".")
  print(f'Valorização (12 meses): {float(valorizacao_acao)}%')

valorizacao_acao()  


print('\n')
print(f'---Métricas Fundamentalistas---')
print('\n')

def dividend_yield(): ## função para mostrar o dividend yeild da ação
  dividend=emaranhado_legal.find_all('strong', class_="value d-block lh-4 fs-4 fw-700")
  dividend_yield=dividend[0].text.replace('%', '')
  if (dividend_yield=='-'):
    print(f'Dividend Yield não informado')
  else:  
    print(f'Dividend Yield: {float(dividend[0].text.replace("%", "").replace(",", "."))}%')

dividend_yield()

def dividendos_atuais(): ## função para mostrar os dividendos distruibuidos da ação
  dividendos_atuais=emaranhado_legal.find_all('div', class_="info w-lg-20")
  dividendos_atuais=dividendos_atuais[1].find('strong').text.replace(",", ".")
  print(f'Dividendos Distribuidos este ano: R$ {float(dividendos_atuais)}')

dividendos_atuais()

#def dividendos_ano_anterior():
#  dividendos_ano_anterior=emaranhado_legal.find_all('div', class_="info w-lg-20")
#  dividendos_ano_anterior=dividendos_ano_anterior[0].find('strong').text.replace(",", ".")
#  print(f'Dividendos Distribuidos ano passado: R$ {float(dividendos_ano_anterior)}')

#dividendos_ano_anterior()

def divida_liquida_ebitda():## função para mostrar a DÍV.LÍQUIDA/EBITDA da ação
  divida_liquida=emaranhado_legal.find_all('div', class_="d-flex align-items-center justify-between pr-1 pr-xs-2")
  divida=divida_liquida[15].find('strong').text.replace(',', '.')
  if (divida=='-'):
    print(f'DÍV.LÍQUIDA/EBITDA não informada')
  else:  
    print(f'DÍV.LÍQUIDA/EBITDA: {float(divida_liquida[15].find("strong").text.replace(",", "."))}')

divida_liquida_ebitda()

def lpa(): ## função para mostrar o lpa da ação
  lpa=emaranhado_legal.find_all('div', class_="d-flex align-items-center justify-between pr-1 pr-xs-2")
  LPA=lpa[10].find('strong').text.replace(',', '.')
  if (LPA=='-'):
    print(f'LPA não informado')
  else:  
    print(f'LPA: {float(lpa[10].find("strong").text.replace(",", "."))}')

lpa()

def p_l(): ## Indice de preço sobre lucro (P/L)
  pl=emaranhado_legal.find_all('div', class_="d-flex align-items-center justify-between pr-1 pr-xs-2")
  PL=pl[1].find('strong').text.replace(',', '.')
  if (PL=='-'):
    print(f'P/L não informado')
  else:  
    print(f'P/L: {float(pl[1].find("strong").text.replace(",", "."))}')

p_l()

def p_vp(): ## função para mostrar P/VP da ação 
  p_vp=emaranhado_legal.find_all('div', class_="d-flex align-items-center justify-between pr-1 pr-xs-2")
  P_VP=p_vp[3].find('strong').text.replace(',', '.')
  if (P_VP=='-'):
    print(f'P/VP não informado')
  else:  
    print(f'P/VP: {float(p_vp[3].find("strong").text.replace(",", "."))}')

p_vp()

def roe(): ## função para mostrar o ROE da ação
  roe=emaranhado_legal.find_all('div', class_="d-flex align-items-center justify-between pr-1 pr-xs-2")
  ROE=roe[24].find('strong').text.replace(',', '.').replace('%', '')
  if (ROE=='-'):
    print(f'ROE não informado')
  else:  
    print(f'ROE: {float(roe[24].find("strong").text.replace(",", ".").replace("%", ""))}%')

roe()

def roic(): ## função para mostrar o ROIC da ação
  roic=emaranhado_legal.find_all('div', class_="d-flex align-items-center justify-between pr-1 pr-xs-2")
  ROIC=roic[26].find('strong').text.replace(',', '.').replace('%', '')
  if (ROIC=='-'):
    print(f'ROIC não informado')
  else:  
    print(f'ROIC: {float(roic[26].find("strong").text.replace(",", ".").replace("%", ""))}%')

roic()

