

import dataframe_class_base as dcb
import sqlite_db_generation as sqlgen





def fill_date(date_df, maxA,maxB,maxC,selected_category,max_loop_iter):
    cont_iter = 0
    if(selected_category == "A"):
        contador = 0
        while(contador <= maxA):
            if(sqlgen.check_if_category_has_quantity("abc_quantity.db", "abc", selected_category)):
                rnd_art = sqlgen.select_random_article("abc_quantity.db", "abc", selected_category)
                #print("random: ", rnd_art[0], rnd_art[1], rnd_art[2])
                if(dcb.check_article_already_in_df(rnd_art[0],date_df)):
                    #print(rnd_art[0], "already in df")
                    cont_iter+=1
                    if(cont_iter>max_loop_iter):
                        break
                    else:
                        continue
                else:
                    if(sqlgen.check_if_article_has_quantity("abc_quantity.db", "abc", rnd_art[0])):
                        date_df = dcb.add_article_to_dataframe(rnd_art[0],rnd_art[1],rnd_art[2],date_df)
                        sqlgen.remove_quant_for_article("abc_quantity.db", "abc",rnd_art[0])
                        cont_iter=0
                        contador+=1
                    else:
                        continue
            else:
                break
        return date_df
    elif(selected_category == "B"):
        contador = 0
        while(contador <=  maxB):
            if(sqlgen.check_if_category_has_quantity("abc_quantity.db", "abc", selected_category)):
                rnd_art = sqlgen.select_random_article("abc_quantity.db", "abc", selected_category)
                #print("random: ", rnd_art[0], rnd_art[1], rnd_art[2])
                if(dcb.check_article_already_in_df(rnd_art[0],date_df)):
                    #print(rnd_art[0], "already in df")
                    cont_iter+=1
                    if(cont_iter>max_loop_iter):
                        break
                    else:
                        continue
                else:
                    if(sqlgen.check_if_article_has_quantity("abc_quantity.db", "abc", rnd_art[0])):
                        date_df = dcb.add_article_to_dataframe(rnd_art[0],rnd_art[1],rnd_art[2],date_df)
                        sqlgen.remove_quant_for_article("abc_quantity.db", "abc",rnd_art[0])
                        contador+=1
                        cont_iter=0
                    else:
                        continue
            else:
                break
        return date_df
    else:
        contador = 0
        while(contador <=  maxC):
            if(sqlgen.check_if_category_has_quantity("abc_quantity.db", "abc", selected_category)):
                rnd_art = sqlgen.select_random_article("abc_quantity.db", "abc", selected_category)
                #print("random: ", rnd_art[0], rnd_art[1], rnd_art[2])
                if(dcb.check_article_already_in_df(rnd_art[0],date_df)):
                    #print(rnd_art[0], "already in df")
                    cont_iter+=1
                    if(cont_iter>max_loop_iter):
                        break
                    else:
                        continue
                else:
                    if(sqlgen.check_if_article_has_quantity("abc_quantity.db", "abc", rnd_art[0])):
                        date_df = dcb.add_article_to_dataframe(rnd_art[0],rnd_art[1],rnd_art[2],date_df)
                        sqlgen.remove_quant_for_article("abc_quantity.db", "abc",rnd_art[0])
                        contador+=1
                        cont_iter=0
                    else:
                        continue
            else:
                break
        return date_df    
    
    
def check_articles_to_count(df_date,a_articles_per_day,b_articles_per_day,c_articles_per_day):
    articles_per_day = a_articles_per_day+b_articles_per_day+c_articles_per_day
    if(len(df_date)>=articles_per_day):
        return True
    else:
        return False

def Assignation_process(dictionary_dates, a_articles_per_day,b_articles_per_day,c_articles_per_day):
    while(sqlgen.check_if_item_without_count("abc_quantity.db", "abc")):
        rnd_date=dcb.random_date_df(dictionary_dates)
        if(check_articles_to_count(dictionary_dates[rnd_date], a_articles_per_day, b_articles_per_day,c_articles_per_day)):
            continue
        else:
            dictionary_dates[rnd_date] = fill_date(dictionary_dates[rnd_date],a_articles_per_day, b_articles_per_day,c_articles_per_day,"A",10)
            dictionary_dates[rnd_date] = fill_date(dictionary_dates[rnd_date],a_articles_per_day, b_articles_per_day,c_articles_per_day,"B",10)
            dictionary_dates[rnd_date] = fill_date(dictionary_dates[rnd_date],a_articles_per_day, b_articles_per_day,c_articles_per_day,"C",10)
    return dictionary_dates