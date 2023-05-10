import pandas as pd
import calendar
import sqlite3
from datetime import datetime

def convert_string_to_date(string_list):
    date_list = [datetime.strptime(x, "%d-%m-%y") for x in string_list]
    return date_list

def weekdays_list(month, year):
    num_days = calendar.monthrange(year, month)[1]
    days_list = [day for day in range(1, num_days+1) if calendar.weekday(year, month, day) != calendar.SUNDAY]
    return days_list


def generate_date_from_list(month, year, days_int_list):
    dates_list = []
    for i in days_int_list:
        date = datetime(year=year, month=month, day=i)
        dates_list.append(date)
    return dates_list

def extract_holidays_from_weekdays(weekdays_of_month, holidays_of_month):
    real_business_days = []
    for i in weekdays_of_month:
        if i in holidays_of_month:
            continue
        else:
            real_business_days.append(i)
    return real_business_days

def convert_date_object_to_string(date):
    date_string = date.strftime('%d/%m/%Y')
    return date_string

def create_list_of_dates(real_business_days_list):
    real_business = []
    for i in real_business_days_list:
        real_business.append(convert_date_object_to_string(i))
        print(i)
    return real_business

def create_dataframe_dictionary(lista):
    dataframe_dict = dict()
    for i in lista:
      date = i.replace("/","-")
      dataframe_dict[date] = pd.DataFrame(columns=["articulo","descripcion","chess","wms","fisico"])
    return dataframe_dict