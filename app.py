import streamlit as st

# --- CONFIGURAÇÃO DA PÁGINA ---
st.set_page_config(
    page_title="Central de Regularidade",
    page_icon="🏢",
    layout="centered"
)

# --- ESTILIZAÇÃO CSS (Visual "Bonitinho") ---
st.markdown("""
    <style>
    /* Centraliza o título principal */
    .main-title {
        text-align: center;
        font-weight: bold;
        color: #2C3E50;
        font-size: 2.5rem;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        color: #5D6D7E;
        margin-bottom: 20px;
    }
    /* Aumenta um pouco os botões para ficarem mais clicáveis */
    .stLinkButton > a {
        font-weight: 600;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown('<div class="main-title">🏢 Central de Certidões</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Foco: São Paulo & Federal</div>', unsafe_allow_html=True)

# --- SEÇÃO 1: FISCAL & CADASTRAL (VERDE) ---
# Usamos st.success para dar o tom VERDE (Dinheiro/Regularidade)
with st.container():
    st.subheader("📗 Regularidade Fiscal e Cadastral", divider="green")
    
    # Caixa verde clara para agrupar
    with st.success():
        col1, col2, col3 = st.columns(3)
        with col1:
            st.link_button("🏢 Receita (CNPJ)", "https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp", use_container_width=True)
        with col2:
            st.link_button("🏦 Caixa (FGTS)", "https://consulta-crf.caixa.gov.br/consultacrf/pages/consultaEmpregador.jsf", use_container_width=True)
        with col3:
            st.link_button("🏙️ Pref. SP (DUC)", "https://duc.prefeitura.sp.gov.br/certidoes/forms_anonimo/frmConsultaEmissaoCertificado.aspx", use_container_width=True)
        
        # Linha de baixo
        col4, col5 = st.columns(2)
        with col4:
            st.link_button("📍 Sefaz SP (Estadual)", "https://www10.fazenda.sp.gov.br/CertidaoNegativaDeb/Pages/EmissaoCertidaoNegativa.aspx", use_container_width=True)
        with col5:
            st.link_button("📂 Jucesp (Ficha)", "https://www.jucesponline.sp.gov.br/Default.aspx", use_container_width=True)

# --- SEÇÃO 2: TRABALHISTA (AZUL) ---
# Usamos st.info para dar o tom AZUL (Corporativo)
with st.container():
    st.subheader("📘 Regularidade Trabalhista", divider="blue")
    
    with st.info():
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            st.link_button("👷 TST (CNDT Nacional)", "https://cndt-certidao.tst.jus.br/inicio.faces", use_container_width=True)
        with col_t2:
            st.link_button("⚖️ TRT-2 (Regional SP)", "https://pje.trt2.jus.br/certidoes/trabalhista/emissao", use_container_width=True)

# --- SEÇÃO 3: JURÍDICO & PROTESTO (VERMELHO/LARANJA) ---
# Usamos st.warning ou st.error para dar destaque de ALERTA
with st.container():
    st.subheader("tc⚖️ Justiça e Protestos", divider="red")
    
    with st.error(): # Fundo avermelhado
        col_j1, col_j2, col_j3 = st.columns(3)
        with col_j1:
            st.link_button("🏛️ Falência TJSP", "https://esaj.tjsp.jus.br/sco/abrirCadastro.do", use_container_width=True)
        with col_j2:
            st.link_button("⚖️ TRF-3 (Federal)", "https://web.trf3.jus.br/certidao-regional/CertidaoCivelEleitoralCriminal/SolicitarDadosCertidao", use_container_width=True)
        with col_j3:
            st.link_button("🚫 Protesto (IEPTB)", "https://protestosp.com.br/consulta-de-protesto", use_container_width=True)

# --- BLOCO DE NOTAS (CINZA/NEUTRO) ---
st.markdown("---")
with st.expander("📝 **Bloco de Notas Rápido (CNPJs)**", expanded=True):
    st.caption("Área de transferência temporária (Cole seus dados aqui)")
    st.text_area(
        label="Area", 
        label_visibility="collapsed",
        placeholder="Cole aqui os CNPJs...\n00.000.000/0001-91",
        height=120
    )
