# 📊 Calculadora de Multa EFD Contribuições

Uma aplicação web moderna e intuitiva para calcular multas por atraso na entrega da EFD Contribuições (Escrituração Fiscal Digital de Contribuições), desenvolvida com Streamlit.

## 🎯 Sobre o Projeto

Esta calculadora foi desenvolvida para auxiliar contadores, empresários e profissionais da área fiscal a calcular rapidamente o valor das multas aplicáveis quando há atraso na entrega da EFD Contribuições, considerando:

- **Regime tributário** (Lucro Real ou Lucro Presumido)
- **Faturamento bruto** do período
- **Dias de atraso** na entrega
- **Percentual de redução** aplicável

## ✨ Funcionalidades

### 🧮 **Cálculo Automático**
- Cálculo baseado na legislação vigente (IN RFB nº 1.252/2012 e Lei nº 8.218/1991)
- Considera limite de 1% do faturamento bruto
- Aplica reduções conforme a situação

### 📊 **Interface Moderna**
- Design responsivo e intuitivo
- Métricas visuais em tempo real
- Gráficos interativos com Plotly
- Modo escuro/claro

### 📈 **Recursos Avançados**
- Comparação entre regimes tributários
- Histórico de cálculos
- Detalhamento completo dos valores
- Visualização gráfica da distribuição da multa

## 🚀 Como Usar

### **Pré-requisitos**
- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)

### **Instalação**

1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/Calculadora-de-Multa-EFD-Contribui-es.git
cd Calculadora-de-Multa-EFD-Contribui-es
```

2. **Crie um ambiente virtual (recomendado):**
```bash
python -m venv .venv
```

3. **Ative o ambiente virtual:**
```bash
# Windows
.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```

4. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

### **Execução**

```bash
streamlit run calculadora.py
```

A aplicação será aberta automaticamente no navegador em `http://localhost:8501`

## 📋 Como Funciona

### **1. Preenchimento dos Dados**
- **Mês/Ano de Referência:** Período da EFD Contribuições
- **Regime Tributário:** Lucro Real ou Lucro Presumido
- **Faturamento Bruto:** Valor do faturamento do período
- **Redução:** Percentual de redução aplicável (0% a 100%)
- **Datas:** Vencimento e entrega da obrigação

### **2. Cálculo Automático**
- **Multa Base:** R$ 1.500/mês (Lucro Real) ou R$ 500/mês (Lucro Presumido)
- **Limite:** 1% do faturamento bruto
- **Multa Final:** Menor valor entre base e limite, com redução aplicada

### **3. Visualização dos Resultados**
- Card principal com valor final destacado
- Tabela detalhada com todos os cálculos
- Gráfico de pizza da distribuição
- Comparação entre regimes
- Histórico dos últimos cálculos

## 📚 Base Legal

### **Multa Base (Art. 57 da IN RFB nº 1.252/2012)**
- **Lucro Real:** R$ 1.500,00 por mês-calendário ou fração
- **Lucro Presumido:** R$ 500,00 por mês-calendário ou fração

### **Limite da Multa (Art. 57, §3º da IN RFB nº 1.252/2012)**
- Não pode ultrapassar 1% do faturamento bruto do período

### **Reduções (Art. 6º da Lei nº 8.218/1991)**
- **50%:** Se cumprida antes de qualquer procedimento de ofício
- **25%:** Se cumprida no prazo fixado em intimação

## 🛠️ Tecnologias Utilizadas

- **[Streamlit](https://streamlit.io/)** - Framework web para Python
- **[Plotly](https://plotly.com/)** - Gráficos interativos
- **[Pandas](https://pandas.pydata.org/)** - Manipulação de dados
- **Python 3.8+** - Linguagem de programação

## 📁 Estrutura do Projeto

```
Calculadora-de-Multa-EFD-Contribui-es/
├── calculadora.py          # Aplicação principal
├── requirements.txt        # Dependências do projeto
├── README.md              # Documentação
└── .devcontainer/         # Configuração para desenvolvimento
    └── devcontainer.json  # Configuração do Codespaces
```

## 🌐 Deploy

### **Streamlit Community Cloud (Recomendado)**
1. Faça push do código para o GitHub
2. Acesse [share.streamlit.io](https://share.streamlit.io)
3. Conecte sua conta GitHub
4. Selecione o repositório e arquivo principal
5. Clique em "Deploy"

### **Outras Opções**
- **Heroku:** Use o Procfile fornecido
- **Docker:** Use o Dockerfile incluído
- **VPS:** Instale Python e execute diretamente

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ⚠️ Aviso Legal

Esta calculadora é uma ferramenta de auxílio e não substitui a consulta a um contador ou advogado especializado. Os cálculos são baseados na legislação vigente, mas podem haver mudanças normativas. Sempre consulte um profissional qualificado para questões fiscais específicas.

## 📞 Suporte

Se encontrar algum problema ou tiver sugestões:

1. Abra uma [issue](https://github.com/seu-usuario/Calculadora-de-Multa-EFD-Contribui-es/issues)
2. Entre em contato através dos canais disponíveis

---

**Desenvolvido com ❤️ para facilitar o trabalho dos profissionais da área fiscal**
