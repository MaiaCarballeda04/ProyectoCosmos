import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Cosmos", layout="wide")

st.title("🚀 Cosmos: Donde el cielo no es el límite, sino el comienzo")
st.markdown("### Proyecto Bootcamp de Into Space - Equipo 2")

# Navegación por pestañas
tabs = st.tabs(["Inicio", "Pioneros", "Sonificación y Táctil", "Derecho Espacial", "Astronomia"])

with tabs[0]:
    st.header("Bienvenido a nuestra plataforma")
    st.write("Esta web busca que la ciencia este al alcance de todos.")
    st.info("Bienvenid@ Cosmonauta.")

with tabs[1]:
    st.header("Pioneros")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Argentina")
        st.write("**Pablo de León:** Especialista en hábitats marcianos.")
        st.write("""
        * **Especialidad:** Ingeniero aeroespacial.
        * **Logros:** Diseñador principal de trajes espaciales y hábitats inflables para misiones a Marte en el Kennedy Space Center de la NASA.
        * **Impacto:** Líder del Laboratorio de Vuelo Espacial Humano de la Universidad de Dakota del Norte.
        """)
        st.write("**Mono Juan:** primer pionero. conoce un poco de su historia escuchando el siguiente audio de La Universidad Nacional de Cordoba")
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
        st.subheader("México: Rodolfo Neri Vela")
        st.write("""
        * **Hito:** Primer astronauta mexicano y latinoamericano en viajar al espacio.
        * **Misión:** Participó en la misión STS-61-B del Transbordador Atlantis (1985), realizando experimentos científicos fundamentales.
        """)
        st.link_button("Biografía", "https://www.gob.mx/mexico")
        
        st.subheader("Venezuela: Humberto Fernández-Morán")
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
with tabs[4]:
    st.header("Ciencia para todos")
    st.write("Aunque vivamos en realidades distintas, cuando miramos hacia arriba todos vemos el mismo sol, la misma luna y las mismas estrellas. Este proyecto explica por qué esas luces de arriba tienen todo que ver con nuestra vida acá abajo.")
    st.info("Bienvenid@s a su primera mision espacial el Origen.")

    st.header("De la roca a la vida")
    st.write("Hace 4.600 millones de años, la Tierra era como una casa sin muebles. Los asteroides trajeron agua y aminoácidos. **Cada átomo de nuestro cuerpo tiene una historia que empezó en una piedra que viajó por el espacio.**")
    st.divider()
    st.header("Explorar es aprender")
    st.write("Empezamos con el Sputnik 1 (tamaño de una pelota de voley). A veces las cosas salen mal, pero aprendemos del error. Hoy, las estaciones espaciales nos ayudan a fabricar medicinas y cultivar comida para vivir mejor en la Tierra.")
    st.divider()
    st.header("Ciencia de Datos: Limpiando el 'ruido'")
    st.write("Como en una cancha de fútbol llena de gente gritando, el espacio tiene 'ruido'. La ciencia de datos es nuestro método para filtrar ese griterío y quedarnos solo con la 'voz' de la estrella. Pasamos de una mancha borrosa a una imagen nítida.")

    st.header("🚀 Explorando lo desconocido: Lecciones de la humanidad")
    st.write("""
    Empezamos lanzando el Sputnik 1, un satélite del tamaño de una pelota de voley. Como un niño que aprende a caminar, nos hemos caído muchas veces: cohetes que fallan o equipos que se rompen.
    
    Pero, como cuando arreglamos algo en casa y nos sale mal la primera vez, **aprendemos del error**. Hoy, gracias a las estaciones espaciales, fabricamos medicinas lejos de la gravedad para cuidar nuestra casa más importante: la Tierra.
    """)
    st.header("🔭 Ciencia de Datos: Limpiando el ruido del universo")
    st.write("""
    ¿Cómo sacamos fotos claras desde tan lejos? Imaginen una cancha de fútbol llena de gente gritando; si un amigo les quiere hablar, no se entiende nada por el ruido.
    
    En el espacio pasa lo mismo: hay polvo y luz estorbando. La **ciencia de datos** es como limpiar ese griterío para quedarnos solo con la "voz" de la estrella o el agujero negro. Es pasar de la mancha borrosa a la imagen nítida.
    """)
    
