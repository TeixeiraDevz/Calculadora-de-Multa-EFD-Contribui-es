import streamlit as st
import pandas as pd
from datetime import date

st.title("Calculadora de Multa EFD Contribuições")
st.markdown("""
<div style='text-align: center; color: #444;'>
    <b>Simule rapidamente o valor da multa de acordo com o regime tributário, faturamento e atraso.</b>
</div>
""", unsafe_allow_html=True)

with st.expander("ℹ️ Como funciona o cálculo? (clique para ver)"):
    st.markdown("""
    **Base legal e regras utilizadas:**
    - **Multa Base:**
        - Lucro Real: R$ 1.500,00 por mês-calendário ou fração.
        - Lucro Presumido: R$ 500,00 por mês-calendário ou fração.
        - (Art. 57 da IN RFB nº 1.252/2012 e Art. 12 da Lei nº 8.218/1991)
    - **Cálculo dos meses de atraso:**
        - Cada 30 dias (ou fração) conta como 1 mês de atraso.
    - **Limite da multa:**
        - Não pode ultrapassar 1% do faturamento bruto do período.
        - (Art. 57, §3º da IN RFB nº 1.252/2012)
    - **Redução (%):**
        - 50%: Se a obrigação for cumprida antes de qualquer procedimento de ofício.
        - 25%: Se cumprida no prazo fixado em intimação.
        - (Art. 6º da Lei nº 8.218/1991)
    """)


col1, col2 = st.columns(2)
with col1:
    mes_ano = st.text_input("Mês/Ano", "01/2025")
    regime = st.selectbox("Regime Tributário", ["Lucro Real", "Lucro Presumido"])
    reducao = st.slider("Redução (%)", min_value=0, max_value=100, value=50, step=5)
with col2:
    faturamento = st.number_input("Faturamento Bruto (R$)", min_value=0.0, value=500000.0, step=1000.0, format="%.2f")
    st.markdown("<span style='font-size:0.95em;'>Formato: <b>DD/MM/AAAA</b></span>", unsafe_allow_html=True)
    data_vencimento = st.date_input("Data de Vencimento", value=date.today(), format="DD/MM/YYYY")
    data_entrega = st.date_input("Data de Entrega", value=date.today(), format="DD/MM/YYYY")

if data_entrega is not None and data_vencimento is not None and data_entrega > data_vencimento:
    dias_atraso = (data_entrega - data_vencimento).days
else:
    dias_atraso = 0

st.write(f"Dias de Atraso: **{dias_atraso}**")

def calcular_multa_base(regime, dias_atraso):
    meses_atraso = (dias_atraso // 30) + 1
    if regime == "Lucro Real":
        return 1500 * meses_atraso
    else:
        return 500 * meses_atraso

if st.button("Calcular Multa", type="primary"):
    multa_base = calcular_multa_base(regime, dias_atraso)
    multa_limitada = faturamento * 0.01
    multa_aplicavel = min(multa_base, multa_limitada)
    multa_final = multa_aplicavel * (1 - (reducao / 100))

    st.success("Cálculo realizado com sucesso!")
    st.markdown("""
    <style>
    .result-table td {{padding: 6px 16px; font-size: 1.1em;}}
    </style>
    <table class='result-table'>
        <tr><td><b>Multa Base (R$):</b></td><td>R$ {:,.2f}</td></tr>
        <tr><td><b>Multa Limitada (1%):</b></td><td>R$ {:,.2f}</td></tr>
        <tr><td><b>Multa Aplicável (R$):</b></td><td>R$ {:,.2f}</td></tr>
        <tr><td><b>Multa Final com Redução (R$):</b></td><td><b style='color: #007b00;'>R$ {:,.2f}</b></td></tr>
    </table>
    """.format(multa_base, multa_limitada, multa_aplicavel, multa_final), unsafe_allow_html=True)
    st.info(f"Referente ao período: {mes_ano}")
else:
    st.warning("Preencha os campos e clique em 'Calcular Multa' para ver o resultado.")
