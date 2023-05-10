import pandas as pd
import os.path


#adding count quantity for each code based on ABC
def cantidad_segun_abc(df):
    df_abc = df[['articulo','descripcion','clasificacion']]
    df_abc = df_abc.dropna()
    lista_cantidad = []
    for i in df_abc['clasificacion']:
        if i == "A":
            lista_cantidad.append(3)
        elif i=="B":
            lista_cantidad.append(2)
        else:
            lista_cantidad.append(1)
    df_abc['cantidad'] = lista_cantidad
    return df_abc
