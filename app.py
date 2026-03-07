import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Cosmos", layout="wide")

st.title("🚀 Cosmos: La Astronomía donde el cielo no es limite, si no el comienzo")
st.markdown("### Proyecto Bootcamp de Into Space")

# Navegación por pestañas
tabs = st.tabs(["Inicio", "Pioneros Regionales", "Sonificación y Táctil", "Derecho Espacial"])

with tabs[0]:
    st.header("Bienvenido a nuestra plataforma")
    st.write("Esta web busca que la ciencia este al alcance de todos.")
    st.info("Bienvenido Cosmonauta.")

with tabs[1]:
    st.header("Pioneros de nuestra Región")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Argentina")
        st.write("**Pablo de León:** Especialista en hábitats marcianos.")
        st.write("""
        * **Especialidad:** Ingeniero aeroespacial.
        * **Logros:** Diseñador principal de trajes espaciales y hábitats inflables para misiones a Marte en el Kennedy Space Center de la NASA.
        * **Impacto:** Líder del Laboratorio de Vuelo Espacial Humano de la Universidad de Dakota del Norte.
        """)
        st.write("**Mono Juan:** primer pionero. conoce un poco de su historia escuchando el siguiente audio.")
        # --- AQUÍ PONES TU AUDIO ---
        st.audio("unciencia_podcast_mono_juan.mp3", format="mp3")
        st.link_button("Noticias CONAE", "https://www.conae.gov.ar")
        

        st.subheader("Chile: María Teresa Ruiz")
        st.write("""
        * **Formación:** Máster y Doctora en Astrofísica por Princeton, siendo la primera mujer en estudiar esta carrera allí.
        * **Logros:** En 1997, fue la primera mujer en ganar el Premio Nacional de Ciencias Exactas tras descubrir la primera enana café conocida.
        * **Liderazgo:** En 2015, fue elegida unánimemente como la primera presidenta de la Academia Chilena de Ciencias.
        * **Experiencia:** En 1978, fue investigadora visitante en el Instituto Goddard (NASA).
        """)
        st.link_button("Universidad de Chile", "https://www.conicyt.cl/mujeres-en-ciencia-y-tecnologia/mujeres-destacadas/premios-nacionales/maria-teresa-ruiz-gonzalez/")
        
        st.subheader("Ecuador")
        st.write("""
        * **Historia:** Fundado en 1873, es uno de los observatorios más antiguos de América Latina.
        * **Ciencia:** Centro fundamental para la geodesia y el estudio de la atmósfera ecuatorial desde el centro del mundo.
        """)
        st.link_button("Historia del OAQ", "https://oaq.epn.edu.ec")

    with col2:
        st.subheader("México:Rodolfo Neri Vela")
        st.write("""
        * **Hito:** Primer astronauta mexicano y latinoamericano en viajar al espacio.
        * **Misión:** Participó en la misión STS-61-B del Transbordador Atlantis (1985), realizando experimentos científicos fundamentales.
        """)
        st.link_button("Biografía", "https://www.gob.mx/mexico")
        
        st.subheader("Venezuela:Humberto Fernández-Morán")
        st.write("""
        * **Inventor:** Creador del bisturí de diamante y pionero en la microscopía electrónica.
        * **NASA:** Su tecnología de ultra-microtomía fue crítica para el análisis de muestras lunares en el Proyecto Apolo.
        """)
        st.link_button("Legado IVIC", "https://www.ivic.gob.ve")
        
        st.subheader("Perú")
        st.write(""" Nataly Andrea Rojas Barnett""")
        st.write("""
        * **Perfil:** Investigadora y destacada académica en el ámbito de la ingeniería y la ciencia aplicada al espacio.
        * **Logros:** Reconocida por su capacidad para liderar proyectos de investigación científica que vinculan la tecnología con soluciones espaciales.
        * **Impacto:** Representa a la nueva generación de científicas peruanas que están abriendo camino en la exploración y el análisis de datos geoespaciales.
        """)
        st.link_button("Leer noticia: Conquistando el espacio", "https://www.unmsm.edu.pe/noticias-y-eventos/noticias/noticia-detalle/creyeron-en-mi-cuando-todo-recien-comenzaba-nataly-rojas-ingeniera-sanmarquina-que-busca-conquistar-el-espacio")
        st.write("""Marlon Delgado""")
        st.write("""
        * **Rol:** Divulgador científico y motor de la educación espacial en Perú.
        * **Impacto:** Gran impulsor de la cultura astronómica y la participación juvenil en proyectos de la Agencia Espacial del Perú (CONIDA).
        """)
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
