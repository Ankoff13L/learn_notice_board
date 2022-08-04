from cgitb import html
import requests
from bs4 import BeautifulSoup

# def get_html(url):
#     try:
#         result = requests.get(url) # при помощи reguests берем данные с этого url
#         result.raise_for_status() # для обработки исключений 
#         return result.text # если страница удачно скачена она будет внутри result.text
#     except(requests.RequestException, ValueError): # RequestException получим если какая то сетевая проблема, ValueError если на стороне сервера возникла какая то проблема
#         print("Сетевая ошибка")
#         return False



# def get_sslv_auto(html):
#     soup = BeautifulSoup(html, "html.parser") # теперь soup это будет html преобразованный в дерево в котором мы будем делать поиск
#     all_auto = soup.find(class_="msga2 pp0").find_parent() #теперь делаем поиск нужного нам дочернего элемента: тега и class  и захватывая весь блок движемся к родительскому тегу
#     result_auto = [] # создадим список
#     for auto in all_auto:                  # создадим цикл в котором пройдемся
#         result_auto.append(
#             {
#                 # id = auto.find("").text  # (integer)
#                 # print(id)
#                 "desccruption" : auto.find("dif").text     # описание (string)
#                 #mark =     # марка (string)
#                 #date_made =    # дата изготовления (datetime.date)
#                 #engine_type =    # тип двиагателя (string)
#                 #transmission =     # КПП (string)
#                 #mileage =   # пробег (integer)
#                 #color =    # цвет (string)
#                 #body_type =    # тип кузова (string)
#                 #inspection =  # техосмотр (datetime.date)
#                 #price =    # цена (integer)
#                 #foto = 
#             }
#         )
#     return result_auto



# print(get_sslv_auto(html.text))



# if __name__ == "__main__":
#     html = get_html("https://www.ss.lv/ru/transport/cars/alfa-romeo/")
#     if html: 
#         # with open("scrap_sslv.html", "w", encoding="utf8") as  f: # мы открыли файл на запись 
#         #    f.write(html)  # и записываем в него наши данные из html
#         get_sslv_auto(html)
            