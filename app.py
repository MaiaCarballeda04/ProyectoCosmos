import streamlit as st

# Configuración
st.set_page_config(page_title="Cosmos Inclusivo", layout="wide")

st.title("🌌 Cosmos Inclusivo: Astronomía para Todos")

# Pestañas
tabs = st.tabs(["Inicio", "Pioneros Regionales", "Sonificación (NASA)", "Derecho Espacial"])

with tabs[0]:
    st.header("¡Bienvenidos a nuestra red!")
    st.write("Esta web permite explorar el espacio sin barreras. Usamos tecnología de voz para personas ciegas y visualización de datos para todos.")

with tabs[1]:
    st.header("Pioneros de Nuestra Tierra")
    st.write("Haz clic en los links para leer las noticias sobre nuestros referentes:")
    
    # Sección Argentina con audio integrado
    st.subheader("🇦🇷 Argentina")
    st.write("Pablo de León y la carrera espacial nacional.")
    st.audio("RUTA_A_TU_ARCHIVO_AUDIO.mp3", format="audio/mp3") # Pon aquí la ruta de tu audio
    st.link_button("Leer noticias locales de Argentina", "https://www.conae.gov.ar")
    
    st.subheader("🇨🇱 Chile")
    st.write("María Teresa Ruiz y el descubrimiento de enanas café.")
    st.link_button("Leer noticia en Chile", "https://www.uchile.cl")

    st.subheader("🇪🇨 Ecuador, 🇲🇽 México, 🇵🇪 Perú, 🇻🇪 Venezuela")
    st.write("Explora más sobre nuestros pioneros locales:")
    st.link_button("México: Rodolfo Neri Vela", "https://www.gob.mx/mexico")
    # Puedes seguir agregando más links aquí

with tabs[2]:
    st.header("Sonificación: Escuchando el Universo")
    st.write("La NASA convierte datos de estrellas y agujeros negros en sonido para que todos puedan 'sentir' los datos.")
    st.link_button("NASA: Sonificación del Agujero Negro", "https://chandra.harvard.edu/sound/")
    st.info("Para personas ciegas: Esta web es compatible con lectores de pantalla (TalkBack/VoiceOver). Todos los botones tienen etiquetas descriptivas.")
    st.success("Para personas sordas: Hemos incluido descripciones detalladas de los sonidos y visualizaciones dinámicas.")

with tabs[3]:
    st.header("Derecho Espacial: La Ley del Cielo")
    st.markdown("""
    * **No hay dueños:** El espacio es patrimonio común.
    * **Paz absoluta:** Prohibido armar bases militares.
    * **Responsabilidad:** Si alguien rompe algo en órbita, debe pagar los daños.
    """)
