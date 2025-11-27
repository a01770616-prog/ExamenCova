import streamlit as st

st.set_page_config(
    page_title='Dashboard multi-pagina',
    layout='wide',
    initial_sidebar_state='expanded'
)

home = st.Page(
    'Paginas/home.py',
    title='Home',
    icon=':material/home:'
)

analisis = st.Page(
    'Paginas/analisis_proyectos.py',
    title='Analisis Proyectos',
    icon=':material/show_chart:'
)

pg = st.navigation({
    'Inicio':[home],
    'Visualizacion':[analisis]
})

pg.run()