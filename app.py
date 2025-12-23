import streamlit as st

# Configuração da página (título da aba e layout)
st.set_page_config(
    page_title="Links Úteis - Jurídico & Adm",
    page_icon="⚖️",
    layout="centered"
)

# Título Principal
st.title("🏢 Central de Acesso Rápido")
st.write("Links úteis para consulta de certidões e processos.")

# --- SEÇÃO 1: CERTIDÕES E CARTÓRIOS ---
st.header("📜 Certidões e Cartórios")

col1, col2 = st.columns(2)

with col1:
    st.link_button("Cenprot (Protesto SP)", "https://www.protestosp.com.br/", use_container_width=True)
    st.caption("Consulta gratuita de protesto em SP.")
    
    st.link_button("Receita Federal (CNPJ)", "https://solucoes.receita.fazenda.gov.br/Servicos/cnpjreva/cnpjreva_solicitacao.asp", use_container_width=True)
    st.caption("Emissão de comprovante de CNPJ.")

with col2:
    st.link_button("Certidão Negativa de Débitos", "https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/certidoes-e-situacao-fiscal", use_container_width=True)
    st.caption("CND Federal e Trabalhista.")

    st.link_button("Registradores (Imóveis)", "https://www.registradores.org.br/", use_container_width=True)
    st.caption("Busca de bens e matrículas.")

st.divider()

# --- SEÇÃO 2: TRIBUNAIS ---
st.header("⚖️ Tribunais de Justiça")

col3, col4 = st.columns(2)

with col3:
    st.link_button("TJ-SP (Consulta Processual)", "https://esaj.tjsp.jus.br/cpopg/open.do", use_container_width=True)
    
with col4:
    st.link_button("TRT (Trtrabalhista)", "https://pje.trt2.jus.br/consultaprocessual/", use_container_width=True)

# --- NOTAS PESSOAIS ---
with st.expander("📝 Notas Rápidas (Bloco de Notas)"):
    st.text_area("Cole aqui números de processos ou anotações temporárias:", height=100)
