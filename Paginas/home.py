import streamlit as st
import pandas as pd
from utils.read import data_reader
from utils.filters import *

df = data_reader()

st.markdown(
    """
    <h1 style='text-align: center;'>
        Dashboard principal de proyectos
    </h1>
    """,
    unsafe_allow_html=True
)

st.sidebar.header("Filtros")

# Estados
estados = sorted(df["State"].dropna().unique().tolist())
estado_sel = st.sidebar.multiselect("Estado", estados)

# Categoría
categorias = sorted(df["Category"].dropna().unique().tolist())
categoria_sel = st.sidebar.multiselect("Categoria", categorias)

# Avance
avance_minimo = st.sidebar.slider("Avance minimo (%)", 0, 100, 0)

# Manager
managers = sorted(df["Manager"].dropna().unique().tolist())
manager_sel = st.sidebar.multiselect("Manager", managers)


df_f = df.copy()
df_f = filtrar_por_estado(df_f, estado_sel)
df_f = filtrar_por_categoria(df_f, categoria_sel)
df_f = filtrar_por_manager(df_f, manager_sel)
df_f = filtrar_por_avance(df_f, avance_minimo)

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Proyectos", len(df_f))
col2.metric("Promedio Avance (%)", round(df_f["PercentComplete"].mean(), 1))
col3.metric("Managers unicos", df_f["Manager"].nunique())
col4.metric("Presupuesto medio", f"{df_f['BudgetThousands'].mean():.1f}K")


st.write("")
st.write("----------------------------------------------------------------")
st.write("")
st.dataframe(
        df_f.sort_values("ProjectID"),
        use_container_width=True
    )