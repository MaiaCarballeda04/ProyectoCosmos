import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Cosmos", layout="wide")

st.title("🚀 Cosmos: La Astronomía donde el cielo no es limite, si no el comienzo")
st.markdown("### Proyecto Bootcamp de Into Space")

# Navegación por pestañas
tabs = st.tabs(["Inicio", "Pioneros Regionales", "Sonificación y Táctil", "Derecho Espacial"])

with tabs[0]:
    st.header("Bienvenido a nuestra plataforma")
    st.write("Esta web busca democratizar la astronomía, eliminando barreras para personas con discapacidad visual y auditiva.")
    st.info("La ciencia es un patrimonio universal de la humanidad.")

with tabs[1]:
    st.header("Pioneros de nuestra Región")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🇦🇷 Argentina")
        st.write("**Pablo de León:** Especialista en hábitats marcianos.")
        # --- AQUÍ PONES TU AUDIO ---
        st.audio("unciencia_podcast_mono_juan.mp3", format="mp3")
        st.link_button("Noticias CONAE", "https://www.conae.gov.ar")
        
        st.subheader("🇨🇱 Chile")
        st.write("**María Teresa Ruiz:** Investigadora")
        st.link_button("Universidad de Chile", "https://www.uchile.cl")
        
        st.subheader("🇪🇨 Ecuador")
        st.write("**Observatorio de Quito:** Historia científica centenaria.")
        st.link_button("Historia del OAQ", "https://oaq.epn.edu.ec")

    with col2:
        st.subheader("🇲🇽 México")
        st.write("**Rodolfo Neri Vela:** Primer astronauta mexicano.")
        st.link_button("Biografía", "https://www.gob.mx/mexico")
        
        st.subheader("🇻🇪 Venezuela")
        st.write("**Humberto Fernández-Morán:** Inventor del bisturí de diamante.")
        st.link_button("Legado IVIC", "https://www.ivic.gob.ve")
        
        st.subheader("🇵🇪 Perú")
        st.write("**Marlon Delgado:** Impulsor de la educación espacial.")
        st.link_button("CONIDA Perú", "https://www.gob.pe/conida")

with tabs[2]:
    st.header("Accesibilidad: Sonido y Tacto")
    st.write("Explorando el universo más allá de la vista.")
    
    st.subheader("NASA: Sonificación")
    st.link_button("Escuchar el Universo", "https://ciencia.nasa.gov/universo/escucha-el-universo-sonificacion-de-datos-y-documental-de-la-nasa/")
    
    st.subheader("Inclusión Táctil: El Dedoscopio")
    st.link_button("Descargar Manual del Dedoscopio", "https://especial.mineduc.cl/wp-content/uploads/sites/31/2023/02/Manual-para-la-inclusion-Dedoscopipo-Actualizado.pdf")
    

with tabs[3]:
    st.header("⚖️ Derecho Espacial: La Ley del Cielo")
    st.markdown("""
    1. **Patrimonio común:** Ningún país es dueño de cuerpos celestes.
    2. **Zona de paz:** Prohibido instalar armas nucleares o bases militares.
    3. **Principio de responsabilidad:** Los Estados son responsables de los daños que causen sus objetos en órbita.
    """)
