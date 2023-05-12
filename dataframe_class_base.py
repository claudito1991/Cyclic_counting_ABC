import pandas as pd
import random


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



def add_article_to_dataframe(cod,descrip,category,date_df):
    df_aux = {'articulo': cod, 'descripcion': descrip,'clasificacion':category, 'chess': "", 'wms': "", 'fisico': "" }
    date_df = pd.concat([date_df, pd.DataFrame([df_aux])], ignore_index=True)
    return date_df


def check_article_already_in_df(cod, date_df):
    if cod in date_df.values:
        return True
    else:
        return False

def random_date_df(dates_dictionary):
    rnd_date = random.choice(list(dates_dictionary.keys()))
    return rnd_date