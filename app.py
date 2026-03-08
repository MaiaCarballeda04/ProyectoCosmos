import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Cosmos", layout="wide")

st.title("🚀 Cosmos: Donde el cielo no es el límite, sino el comienzo")
st.markdown("### Proyecto Bootcamp de Into Space - Equipo 2")

# Navegación por pestañas
tabs = st.tabs(["Inicio", "Pioneros", "Sonificación y Táctil", "Derecho Espacial", "Astronomia","Pioneras"])

with tabs[0]:
    st.header("Bienvenido a nuestra plataforma")
    st.write("Esta web busca que la ciencia este al alcance de todos.")
    st.info("Bienvenid@ Cosmonauta.")
    st.image("Academia.jpg", use_container_width=True)


with tabs[1]:
    st.header("Pioneros")
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Argentina")
        st.write("**Pablo de León:** Especialista en hábitats marcianos.")
        st.image("Pablo.jpg", width=200)
        st.write("""
        * **Especialidad:** Ingeniero aeroespacial.
        * **Logros:** Diseñador principal de trajes espaciales y hábitats inflables para misiones a Marte en el Kennedy Space Center de la NASA.
        * **Impacto:** Líder del Laboratorio de Vuelo Espacial Humano de la Universidad de Dakota del Norte.
        """)
        st.link_button("Noticias CONAE", "https://www.conae.gov.ar")
        st.write("**Mono Juan:** primer pionero. conoce un poco de su historia escuchando el siguiente audio de La Universidad Nacional de Cordoba")
        st.image("Juan.jpg", width=200)
        st.audio("unciencia_podcast_mono_juan.mp3", format="mp3")
        st.link_button("Mono Juan","https://unciencia.unc.edu.ar/podcasts/juan-el-primer-astronauta-argentino-2/#:~:text=El%2023%20de%20diciembre%20de,espacio%20utilizando%20tecnolog%C3%ADa%20aeroespacial%20propia")
        
        st.divider()
        st.subheader("Chile: María Teresa Ruiz")
        st.image("Maria.jpg", width=200)
        st.write("""
        * **Formación:** Máster y Doctora en Astrofísica por Princeton, siendo la primera mujer en estudiar esta carrera allí.
        * **Logros:** En 1997, fue la primera mujer en ganar el Premio Nacional de Ciencias Exactas tras descubrir la primera enana café conocida.
        * **Liderazgo:** En 2015, fue elegida unánimemente como la primera presidenta de la Academia Chilena de Ciencias.
        * **Experiencia:** En 1978, fue investigadora visitante en el Instituto Goddard (NASA).
        """)
        st.link_button("Universidad de Chile", "https://www.conicyt.cl/mujeres-en-ciencia-y-tecnologia/mujeres-destacadas/premios-nacionales/maria-teresa-ruiz-gonzalez/")
        st.divider()
        st.subheader("Ecuador")
        st.image("Quito.jpg", width=200)
        st.write("""
        * **Historia:** Fundado en 1873, es uno de los observatorios más antiguos de América Latina.
        * **Ciencia:** Centro fundamental para la geodesia y el estudio de la atmósfera ecuatorial desde el centro del mundo.
        """)
        st.link_button("Historia del OAQ", "https://oaq.epn.edu.ec")

    with col2:
        st.subheader("México: Rodolfo Neri Vela")
        st.image("Rodolfo.jpg", width=200)
        st.write("""
        * **Hito:** Primer astronauta mexicano y latinoamericano en viajar al espacio.
        * **Misión:** Participó en la misión STS-61-B del Transbordador Atlantis (1985), realizando experimentos científicos fundamentales.
        """)
        st.link_button("Biografía", "https://www.gob.mx/mexico")
        st.divider()
        st.subheader("Venezuela: Humberto Fernández-Morán")
        st.image("Humberto.jpg", width=200)
        st.write("""
        * **Inventor:** Creador del bisturí de diamante y pionero en la microscopía electrónica.
        * **NASA:** Su tecnología de ultra-microtomía fue crítica para el análisis de muestras lunares en el Proyecto Apolo.
        """)
        st.link_button("Legado IVIC", "https://www.ivic.gob.ve")
        st.divider()
        st.subheader("Perú")
        st.write(""" Nataly Andrea Rojas Barnett""")
        st.image("Nataly.jpg", width=200)
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
    st.write("""Usamos la sonificación, convertimos los datos de los telescopios en sonidos, 
    gráficos que se mueven al ritmo de los datos, para que se pueda ver el pulso del universo
    """)
    st.link_button("Escuchar el Universo", "https://ciencia.nasa.gov/universo/escucha-el-universo-sonificacion-de-datos-y-documental-de-la-nasa/")
    
    st.subheader("Inclusión Táctil: El Dedoscopio")
    st.write("""Usamos este libro, convertimos los datos de los telescopios en algo tactil, 
    un asteroide pasando frente a una estrella al alcance de tu mano, el universo a veces esta cerca!
    además, usamos modelos táctiles (maquetas con texturas) para que cualquiera pueda tocar cómo es la forma de un asteroide.""")
    st.link_button("Descargar Manual del Dedoscopio", "https://especial.mineduc.cl/wp-content/uploads/sites/31/2023/02/Manual-para-la-inclusion-Dedoscopipo-Actualizado.pdf")
    

with tabs[3]:
    st.header("⚖️ Derecho Espacial: La Ley del Cielo")
    st.markdown("""
    1. **Patrimonio común:** Ningún país es dueño de cuerpos celestes. El espacio es 'patrimonio de la humanidad' nadie, ningún país y ninguna empresa, puede decir 'esto es mío', es de todos, igual que el aire que respiramos.
    2. **Zona de paz:** Prohibido instalar armas nucleares o bases militares. no para pelear,fue un acuerdo clave para que todos los países se sienten a charlar en paz.
    3. **Principio de responsabilidad:** Los Estados son responsables de los daños que causen sus objetos en órbita. esto sirve para que nadie ande tirando basura espacial o haciendo maniobras arriesgadas sin hacerse cargo de las consecuencias.
    """)
with tabs[4]:
    st.header("Ciencia para todos")
    st.write("Aunque vivamos en realidades distintas, cuando miramos hacia arriba todos vemos el mismo sol, la misma luna y las mismas estrellas. Este proyecto explica por qué esas luces de arriba tienen todo que ver con nuestra vida acá abajo.")
    st.info("Bienvenid@s a su primera mision espacial el Origen.")

    st.header("🪨De la roca a la vida")
    st.write("Hace 4.600 millones de años, la Tierra era como una casa sin muebles. Los asteroides trajeron agua y aminoácidos. **Cada átomo de nuestro cuerpo tiene una historia que empezó en una piedra que viajó por el espacio.**")
    st.divider()
    st.header("🔎Explorar es aprender")
    st.write("Empezamos con el Sputnik 1. A veces las cosas salen mal, pero aprendemos del error. Hoy, las estaciones espaciales nos ayudan a fabricar medicinas y cultivar comida para vivir mejor en la Tierra.")
    st.divider()
    st.header("💯Ciencia de Datos: Limpiando el 'ruido'")
    st.write("Como en una cancha de fútbol llena de gente gritando, el espacio tiene 'ruido'. La ciencia de datos es nuestro método para filtrar ese griterío y quedarnos solo con la 'voz' de la estrella. Pasamos de una mancha borrosa a una imagen nítida.")
    st.divider()
    st.header("🚀 Explorando lo desconocido: Lecciones de la humanidad")
    st.write("""
    Empezamos lanzando el de un satelite de origen ruso llamado "Sputnik 1", un satélite del tamaño de una pelota de voley. Como un niño que aprende a caminar, nos hemos caído muchas veces: cohetes que fallan o equipos que se rompen.
    
    Pero, como cuando arreglamos algo en casa y nos sale mal la primera vez, **aprendemos del error**. Hoy, gracias a las estaciones espaciales, fabricamos medicinas lejos de la gravedad para cuidar nuestra casa más importante: la Tierra.
    """)
    st.divider()
    st.header("🔭 Ciencia de Datos: Limpiando el ruido del universo")
    st.write("""
    ¿Cómo sacamos fotos claras desde tan lejos? Imaginen una cancha de fútbol llena de gente gritando; si un amigo les quiere hablar, no se entiende nada por el ruido.
    
    En el espacio pasa lo mismo: hay polvo y luz estorbando. La **ciencia de datos** es como limpiar ese griterío para quedarnos solo con la "voz" de la estrella o el agujero negro. Es pasar de la mancha borrosa a la imagen nítida.
    """)
with tabs[5]:
    st.header("👩‍🚀 Pioneras que conquistaron el Cosmos")
    st.write("Mujeres cuya tenacidad hizo posible la exploración espacial.")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Chile: María Teresa Ruiz")
        st.write("Primera mujer en recibir el Premio Nacional de Ciencias Exactas en Chile. Descubrió la primera enana café.")
        
        st.subheader("Perú: Nataly Rojas Barnett")
        st.write("Ingeniera sanmarquina, referente actual en ciencia espacial e investigación aeroespacial.")

        st.subheader("México: Silvia Torres-Peimbert")
        st.write("Primera mujer doctora en Astronomía en México y ex-Presidenta de la Unión Astronómica Internacional.")
        
        st.subheader("Rusia: Valentina Tereshkova")
        st.write("La primera mujer en viajar al espacio (1963) a sus 26 años.")
        
        st.subheader("EEUU: Margaret Hamilton")
        st.write("Directora de software del Apolo 11. Su código evitó que la misión lunar fallara.")

        st.subheader("India: Kalpana Chawla")
        st.write("Primera mujer de origen indio en el espacio. Su valentía y su compromiso con la ciencia continúan inspirando a nuevas generaciones de ingenieros en todo el mundo.")

    with col2:
        st.subheader("Argentina: Noel de Castro")
        st.write("Referente argentina en el desarrollo espacial, clave en la formación de nuevas visiones científicas.")

        st.subheader("Argentina: Adela E. Ringuelet")
        st.write("Astrónoma pionera y cofundadora de la Asociación Argentina de Astronomía. Impulsó estudios sobre estrellas peculiares.")
        
        st.subheader("Colombia: Adriana Ocampo")
        st.write("Directora de Ciencia de la NASA. Líder en la investigación del cráter de Chicxulub.")

        st.subheader("Colombia: Diana Trujillo")
        st.write("Ingeniera aeroespacial (U. de Maryland) y líder fundamental en la misión Curiosity de la NASA.")
        
        st.subheader("Costa Rica: Sandra Cauffman")
        st.write("Directora adjunta de la División de Ciencias de la Tierra en la NASA. Inspiración para toda Latinoamérica.")
        
        st.subheader("EEUU: Nancy Roman")
        st.write("La 'Madre del Hubble', astrónoma clave en el desarrollo del telescopio espacial.")
        
        st.subheader("EEUU: Katherine Johnson")
        st.write("Matemática cuya precisión hizo posibles los vuelos tripulados del Apolo.")

    st.info("Estas mujeres demuestran que el espacio no tiene género, solo necesita talento y determinación.")
    
