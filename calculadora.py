import streamlit as st
import pandas as pd
from datetime import date, datetime
import plotly.express as px
import plotly.graph_objects as go

+st.set_page_config(
    page_title="Calculadora EFD Contribuições",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    /* Estilos base para garantir visibilidade */
    .stApp {
        color: #262730 !important;
    }
    .stMarkdown, .stMarkdown * {
        color: inherit !important;
    }
    
    .main-header {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
    }
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
        opacity: 0.9;
    }
    .info-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #007bff;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        color: #333 !important;
    }
    .info-card * {
        color: #333 !important;
    }
    .result-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 6px 20px rgba(0, 0, 0, 0.15);
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        border: 1px solid #e9ecef;
        text-align: center;
    }
    .stButton > button {
        background: linear-gradient(45deg, #007bff, #0056b3);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0, 123, 255, 0.3);
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <h1>📊 Calculadora de Multa EFD Contribuições</h1>
    <p>Simule rapidamente o valor da multa de acordo com o regime tributário, faturamento e atraso</p>
</div>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 📋 Informações Legais")
    st.markdown("""
    <div class="info-card" style="color: #333 !important;">
        <div style="color: #333 !important;">
            <strong style="color: #333 !important;">Multa Base:</strong><br>
            <span style="color: #333 !important;">• Lucro Real: R$ 1.500,00/mês</span><br>
            <span style="color: #333 !important;">• Lucro Presumido: R$ 500,00/mês</span><br><br>
            <strong style="color: #333 !important;">Limite:</strong> <span style="color: #333 !important;">1% do faturamento</span><br><br>
            <strong style="color: #333 !important;">Reduções:</strong><br>
            <span style="color: #333 !important;">• 50%: Antes de intimação</span><br>
            <span style="color: #333 !important;">• 25%: No prazo da intimação</span>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### ⚙️ Configurações")
    modo_escuro = st.checkbox("🌙 Modo Escuro", value=False)
    
    if modo_escuro:
        st.markdown("""
        <style>
        .stApp { 
            background-color: #1a1a1a !important;
            color: #ffffff !important;
        }
        .main .block-container { 
            background-color: #1a1a1a !important;
            color: #ffffff !important;
        }
        .info-card {
            background: #2d2d2d !important;
            color: #ffffff !important;
        }
        .info-card * {
            color: #ffffff !important;
        }
        .metric-card {
            background: #2d2d2d !important;
            color: #ffffff !important;
            border: 1px solid #444 !important;
        }
        .metric-card * {
            color: #ffffff !important;
        }
        </style>
        """, unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📝 Dados da Empresa")
    mes_ano = st.text_input("📅 Mês/Ano de Referência", "01/2025", help="Formato: MM/AAAA")
    regime = st.selectbox("🏢 Regime Tributário", ["Lucro Real", "Lucro Presumido"])
    faturamento = st.number_input(
        "💰 Faturamento Bruto (R$)", 
        min_value=0.0, 
        value=500000.0, 
        step=1000.0, 
        format="%.2f",
        help="Faturamento bruto do período de referência"
    )

with col2:
    st.markdown("### 📊 Configuração da Multa")
    reducao = st.slider("📉 Redução (%)", min_value=0, max_value=100, value=50, step=5, help="Percentual de redução aplicável")
    
    st.markdown("<span style='font-size:0.9em; color: #666;'>📅 <b>Formato: DD/MM/AAAA</b></span>", unsafe_allow_html=True)
    data_vencimento = st.date_input("⏰ Data de Vencimento", value=date.today(), format="DD/MM/YYYY")
    data_entrega = st.date_input("📤 Data de Entrega", value=date.today(), format="DD/MM/YYYY")

if data_entrega is not None and data_vencimento is not None and data_entrega > data_vencimento:
    dias_atraso = (data_entrega - data_vencimento).days
else:
    dias_atraso = 0

col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"""
    <div class="metric-card">
        <h3 style='color: #dc3545; margin: 0;'>⏰</h3>
        <h2 style='color: #dc3545; margin: 0;'>{dias_atraso}</h2>
        <p style='margin: 0; color: #666;'>Dias de Atraso</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    meses_atraso = (dias_atraso // 30) + 1 if dias_atraso > 0 else 0
    st.markdown(f"""
    <div class="metric-card">
        <h3 style='color: #fd7e14; margin: 0;'>📅</h3>
        <h2 style='color: #fd7e14; margin: 0;'>{meses_atraso}</h2>
        <p style='margin: 0; color: #666;'>Meses de Atraso</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="metric-card">
        <h3 style='color: #6f42c1; margin: 0;'>🏢</h3>
        <h2 style='color: #6f42c1; margin: 0; font-size: 1.2rem;'>{regime.split()[0]}</h2>
        <p style='margin: 0; color: #666;'>Regime</p>
    </div>
    """, unsafe_allow_html=True)

def calcular_multa_base(regime, dias_atraso):
    meses_atraso = (dias_atraso // 30) + 1
    if regime == "Lucro Real":
        return 1500 * meses_atraso
    else:
        return 500 * meses_atraso

# Botão de cálculo 
st.markdown("<br>", unsafe_allow_html=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    calcular = st.button("🚀 Calcular Multa", type="primary", use_container_width=True)

if calcular:
    multa_base = calcular_multa_base(regime, dias_atraso)
    multa_limitada = faturamento * 0.01
    multa_aplicavel = min(multa_base, multa_limitada)
    multa_final = multa_aplicavel * (1 - (reducao / 100))
    
    st.markdown(f"""
    <div class="result-card">
        <h1 style='margin: 0 0 1rem 0;'>💰 Multa Final</h1>
        <h2 style='margin: 0; font-size: 3rem;'>R$ {multa_final:,.2f}</h2>
        <p style='margin: 1rem 0 0 0; opacity: 0.9;'>Referente ao período: {mes_ano}</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 📊 Detalhamento do Cálculo")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="info-card">
            <h4 style='margin-top: 0;'>📈 Valores Calculados</h4>
            <table style='width: 100%;'>
                <tr><td><strong>Multa Base:</strong></td><td style='text-align: right;'>R$ {:,.2f}</td></tr>
                <tr><td><strong>Multa Limitada (1%):</strong></td><td style='text-align: right;'>R$ {:,.2f}</td></tr>
                <tr><td><strong>Multa Aplicável:</strong></td><td style='text-align: right;'>R$ {:,.2f}</td></tr>
                <tr><td><strong>Redução ({:g}%):</strong></td><td style='text-align: right; color: #dc3545;'>-R$ {:,.2f}</td></tr>
            </table>
        </div>
        """.format(multa_base, multa_limitada, multa_aplicavel, reducao, multa_aplicavel - multa_final), unsafe_allow_html=True)
    
    with col2:
        # Gráfico de pizza dos valores
        labels = ['Multa Final', 'Redução Aplicada']
        values = [multa_final, multa_aplicavel - multa_final]
        colors = ['#28a745', '#dc3545']
        
        fig = go.Figure(data=[go.Pie(labels=labels, values=values, marker_colors=colors)])
        fig.update_layout(
            title="Distribuição da Multa",
            height=300,
            showlegend=True
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Comparação entre regimes____
    st.markdown("### 🔍 Comparação entre Regimes")
    
    multa_lucro_real = calcular_multa_base("Lucro Real", dias_atraso)
    multa_lucro_presumido = calcular_multa_base("Lucro Presumido", dias_atraso)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown(f"""
        <div class="metric-card">
            <h4 style='color: #007bff; margin-top: 0;'>Lucro Real</h4>
            <h2 style='color: #007bff; margin: 0;'>R$ {min(multa_lucro_real, faturamento * 0.01):,.2f}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div class="metric-card">
            <h4 style='color: #28a745; margin-top: 0;'>Lucro Presumido</h4>
            <h2 style='color: #28a745; margin: 0;'>R$ {min(multa_lucro_presumido, faturamento * 0.01):,.2f}</h2>
        </div>
        """, unsafe_allow_html=True)
    
    # Histórico de cálculos (simulado)
    if 'historico' not in st.session_state:
        st.session_state.historico = []
    
    calculo_atual = {
        'data': datetime.now().strftime("%d/%m/%Y %H:%M"),
        'regime': regime,
        'dias_atraso': dias_atraso,
        'multa_final': multa_final
    }
    st.session_state.historico.append(calculo_atual)
    
    if len(st.session_state.historico) > 5:
        st.session_state.historico = st.session_state.historico[-5:]
    
    st.markdown("### 📋 Histórico de Cálculos")
    df_historico = pd.DataFrame(st.session_state.historico)
    st.dataframe(df_historico, use_container_width=True)
    
    st.success("✅ Cálculo realizado com sucesso!")

else:
    st.info("👆 Preencha os campos e clique em 'Calcular Multa' para ver o resultado.")
