import streamlit as st
from capta_dados_bcb import codigo_sgs, request_data
import plotly.express as px
from datetime import datetime, timedelta

data_init = "01/01/1980"
data_fim = "16/03/2025"
 
# Título da página
st.title("FinanceBR - Dados Financeiros")


st.sidebar.title("🔍FILTROS")
st.sidebar.title("📅 Selecione o Período")

# Datas padrão: últimos 5 anos
data_inicio_padrao = datetime.today() - timedelta(days=5*365)
data_fim_padrao = datetime.today()

# Widgets para selecionar as datas no formato dd/mm/yyyy
col1, col2 = st.sidebar.columns(2)
data_inicio = col1.date_input("Data Inicial", value=data_inicio_padrao, format="DD/MM/YYYY")
data_fim = col2.date_input("Data Final", value=data_fim_padrao, format="DD/MM/YYYY")

# Convertendo para strings no formato esperado pela API (YYYY-MM-DD)
data_inicio_str = data_inicio.strftime("%d/%m/%Y")
data_fim_str = data_fim.strftime("%d/%m/%Y")


st.sidebar.title("📈Selecionar Indicadores")
for nome_indicador, codigo in codigo_sgs.items():
    if st.sidebar.checkbox(nome_indicador, key=nome_indicador):
        df = request_data(codigo, data_inicio_str, data_fim_str)
        
        if df is not None:
            # Criando gráfico de linha com Plotly
            fig = px.line(df, x="data", y="valor", title=f"Evolução do {nome_indicador}")
            st.plotly_chart(fig)





