import pandas as pd
import requests
import streamlit as st


codigo_sgs = {
    "IPCA Mensal": 433,
    "Taxa Selic": 1178,
    "Taxa de Câmbio": 189,
    "IGP-DI": 1,
    "IGP-M": 226,
    "Taxa de Desemprego": 12,
    "Produção Industrial": 7450,
    "Balança Comercial": 7326,
    "Dívida Líquida do Setor Público": 11754,
    "IBC-Br (Atividade Econômica)": 27842,
    "Taxa de Juros Média": 4390,
    "Saldo das Operações de Crédito": 20786,
    "Inadimplência - Pessoas Físicas": 21086,
    "Inadimplência - Pessoas Jurídicas": 21087,
    "Reservas Internacionais": 3545,
    "Investimento Estrangeiro Direto": 10813,
    "Dívida Externa Bruta": 11752,
    "Taxa de Desocupação Média Nacional": 24369,
    "Força de Trabalho Total": 24378,
    "Rendimento Médio Real Efetivo": 24381
}

sgs_selecionado = codigo_sgs["Taxa Selic"]
data_init = "01/01/1980"
data_fim = "16/03/2025"


def request_data(sgs_selecionado, data_init, data_fim):
    url = "https://api.bcb.gov.br/dados/serie/bcdata.sgs."+str(sgs_selecionado)+"/dados?formato=json\
        &dataInicial="+data_init+"&dataFinal="+data_fim


    # Requisição à API
    response = requests.get(url)
    data = response.json()

    # Transformando em DataFrame
    df = pd.DataFrame(data)
    df['data'] = pd.to_datetime(df['data'], dayfirst=True)
    df['valor'] = df['valor'].astype(float)
    return df

request_data(sgs_selecionado,data_init,data_fim)

