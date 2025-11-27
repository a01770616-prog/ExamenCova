import streamlit as st
import pandas as pd
from utils.read import data_reader
from utils.filters import *
from utils.graphics import scatter_avance_presupuesto

df = data_reader()

st.markdown(
    """
    <h1 style='text-align: center;'>
        Visualizacion y comparacion
    </h1>
    """,
    unsafe_allow_html=True
)

st.sidebar.header("Filtros")

#Manager
managers = sorted(df["Manager"].dropna().unique().tolist())
manager_sel = st.sidebar.multiselect("Manager", managers)

# Categoría
categorias = sorted(df["Category"].dropna().unique().tolist())
categoria_sel = st.sidebar.multiselect("Categoria", categorias)

df_f = df.copy()
df_f = filtrar_por_categoria(df_f, categoria_sel)
df_f = filtrar_por_manager(df_f, manager_sel)

fig = scatter_avance_presupuesto(df_f)
st.plotly_chart(fig, use_container_width=True)