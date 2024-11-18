import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Minha Primeira App Streamlit",
    layout="wide"
)

# Título principal
st.title("Bem-vindo à minha primeira aplicação Streamlit! 🎈")

# Barra lateral
st.sidebar.header("Configurações")

# Exemplo de alguns elementos básicos
nome = st.text_input("Digite seu nome:")
if nome:
    st.write(f"Olá, {nome}!")

# Exemplo de upload de arquivo
uploaded_file = st.file_uploader("Escolha um arquivo CSV", type="csv")
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    
    # Mostra os dados
    st.subheader("Seus dados:")
    st.dataframe(df)
    
    # Exemplo de gráfico
    if len(df.columns) >= 2:
        st.subheader("Visualização:")
        coluna_x = st.selectbox("Escolha a coluna para o eixo X:", df.columns)
        coluna_y = st.selectbox("Escolha a coluna para o eixo Y:", df.columns)
        
        fig = px.scatter(df, x=coluna_x, y=coluna_y)
        st.plotly_chart(fig)

# Exemplo de diferentes tipos de input
st.subheader("Exemplos de inputs:")

col1, col2 = st.columns(2)
with col1:
    opcao = st.selectbox("Escolha uma opção:", ["Opção 1", "Opção 2", "Opção 3"])
    st.write("Você selecionou:", opcao)

with col2:
    slider = st.slider("Escolha um valor:", 0, 100, 50)
    st.write("Valor selecionado:", slider)

# Exemplo de checkbox
if st.checkbox("Mostrar texto explicativo"):
    st.markdown("""
    ### Como usar esta aplicação:
    1. Digite seu nome no campo de texto
    2. Faça upload de um arquivo CSV
    3. Explore os dados e visualizações
    4. Teste diferentes inputs
    """)
