import streamlit as st

# Configuração da página
st.set_page_config(
    page_title="Central de Certidões",
    page_icon="🏢",
    layout="centered"
)

# Título e Descrição
st.title("🏢 Central de Certidões & Regularidade")
st.write("Links diretos para emissão de certidões de condomínios e empresas.")
st.write("**Foco:** SP e Federal")

st.divider()

# --- GRUPO 1: FISCAL E CADASTRAL (FEDERAL/MUNICIPAL) ---
st.subheader("🏛️ Regularidade Fiscal e Cadastral")

# Linha 1: Os 3 principais
col1, col2, col3 = st.columns(3)

with col1:
    st.link_button(
        "Receita Federal (CNPJ)", 
        "https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp", 
        use_container_width=True,
        help="Situação Cadastral CNPJ"
    )

with col2:
    st.link_button(
        "Caixa (FGTS)", 
        "https://consulta-crf.caixa.gov.br/consultacrf/pages/consultaEmpregador.jsf", 
        use_container_width=True,
        help="Certificado de Regularidade do FGTS"
    )

with col3:
    st.link_button(
        "Prefeitura SP (DUC)", 
        "https://duc.prefeitura.sp.gov.br/certidoes/forms_anonimo/frmConsultaEmissaoCertificado.aspx", 
        use_container_width=True,
        help="Demonstrativo Unificado do Contribuinte"
    )

# Linha 2: Estadual e Junta Comercial (Novos links)
col_a, col_b = st.columns(2)

with col_a:
    st.link_button(
        "Sefaz SP (CND Estadual)", 
        "https://www10.fazenda.sp.gov.br/CertidaoNegativaDeb/Pages/EmissaoCertidaoNegativa.aspx", 
        use_container_width=True,
        help="Certidão Negativa de Débitos Tributários da Dívida Ativa (Estadual)"
    )

with col_b:
    st.link_button(
        "Jucesp (Ficha Cadastral)", 
        "https://www.jucesponline.sp.gov.br/Default.aspx", 
        use_container_width=True,
        help="Consulta de NIRE e dados societários na Junta Comercial"
    )

# --- GRUPO 2: TRABALHISTA ---
st.subheader("👷 Regularidade Trabalhista")
col4, col5 = st.columns(2)

with col4:
    st.link_button(
        "TST (CNDT Nacional)", 
        "https://cndt-certidao.tst.jus.br/inicio.faces", 
        use_container_width=True,
        help="Certidão Negativa de Débitos Trabalhistas"
    )

with col5:
    st.link_button(
        "TRT-2 (Regional SP)", 
        "https://pje.trt2.jus.br/certidoes/trabalhista/emissao", 
        use_container_width=True,
        help="Certidão de Ações Trabalhistas (SP/Baixada)"
    )

# --- GRUPO 3: JUDICIÁRIO E PROTESTOS ---
st.subheader("⚖️ Justiça Comum e Protestos")
col6, col7, col8 = st.columns(3)

with col6:
    st.link_button(
        "Falência - TJSP (estadual)", 
        "https://esaj.tjsp.jus.br/sco/abrirCadastro.do", 
        use_container_width=True,
        help="Certidão de Distribuição Cível/Criminal"
    )

with col7:
    st.link_button(
        "TRF-3 (Federal)", 
        "https://web.trf3.jus.br/certidao-regional/CertidaoCivelEleitoralCriminal/SolicitarDadosCertidao", 
        use_container_width=True,
        help="Certidão da Justiça Federal da 3ª Região"
    )

with col8:
    st.link_button(
        "Protesto SP (IEPTB)", 
        "https://protestosp.com.br/consulta-de-protesto", 
        use_container_width=True,
        help="Consulta gratuita de protestos em cartório"
    )

st.divider()

# --- NOTAS PESSOAIS ---
with st.expander("📝 Bloco de Notas (CNPJs e Observações)", expanded=True):
    st.text_area(
        "Cole aqui os CNPJs para consulta rápida:", 
        placeholder="Ex: 00.000.000/0001-91\nEx: 11.111.111/0001-91",
        height=150
    )
