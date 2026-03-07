import streamlit as st

# Configuración básica de la página
st.set_page_config(page_title="Cosmos Inclusivo", layout="wide")

# Título Principal
st.title("🌌 Cosmos Inclusivo: Astronomía para todos")
st.markdown("### Estrategia de divulgación científica accesible")

# Navegación con pestañas (más limpio para usuarios)
tab1, tab2, tab3, tab4 = st.tabs(["Inicio", "Pioneros", "Sonificación (NASA)", "Derecho Espacial"])

with tab1:
    st.header("Bienvenido a nuestra plataforma")
    st.write("Este proyecto nace para democratizar la astronomía.")
    st.info("Accesibilidad es nuestra prioridad: diseño compatible con lectores de pantalla para personas ciegas y descripciones textuales para personas sordas.")

with tab2:
    st.header("Pioneros Regionales")
    # Columna para organizar visualmente
    c1, c2 = st.columns(2)
    with c1:
        st.write("🇦🇷 **Argentina:** Pablo de León (NASA Mars Suits)")
        st.link_button("Noticias Argentina", "https://www.conae.gov.ar")
        
        st.write("🇨🇱 **Chile:** María Teresa Ruiz (Enanas café)")
        st.link_button("Noticias Chile", "https://www.uchile.cl")
    
    with c2:
        st.write("🇲🇽 **México:** Rodolfo Neri Vela (Primer Astronauta)")
        st.link_button("Noticias México", "https://www.gob.mx/mexico")
        
        st.write("🇪🇨 **Ecuador:** Obs. Astronómico de Quito")
        st.link_button("Historia de Quito", "https://oaq.epn.edu.ec")

with tab3:
    st.header("Sonificación Astronómica")
    st.write("La NASA permite escuchar el universo mediante datos convertidos en sonido.")
    st.link_button("Escuchar datos de la NASA", "https://chandra.harvard.edu/sound/")
    st.warning("Nota para usuarios sordos: Los datos se representan mediante variaciones de frecuencia y amplitud que pueden ser visualizadas en gráficos de onda.")

with tab4:
    st.header("Derecho Espacial: La Ley del Cielo")
    st.markdown("""
    1. **Espacio como patrimonio:** Ningún país es dueño de cuerpos celestes.
    2. **Zona pacífica:** Prohibición estricta de armas nucleares y bases militares.
    3. **Principio de responsabilidad:** Responsabilidad estatal por daños causados en órbita.
    """)
    st.success("El espacio es un bien común de la humanidad.")

# Barra lateral para créditos
st.sidebar.markdown("---")
st.sidebar.write("Proyecto: Astronomía Ciudadana")
st.sidebar.write("Tecnología: Python & Streamlit")
