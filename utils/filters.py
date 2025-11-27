import pandas as pd

def filtrar_por_estado(df, estados):
    if estados:
        df = df[df["State"].isin(estados)]
    return df

def filtrar_por_categoria(df, categorias):
    if categorias:
        df = df[df["Category"].isin(categorias)]
    return df

def filtrar_por_manager(df, managers):
    if managers:
        df = df[df["Manager"].isin(managers)]
    return df

def filtrar_por_avance(df, avance_minimo):
    df = df[df["PercentComplete"] >= avance_minimo]
    return df
