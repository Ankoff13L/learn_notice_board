from cgitb import html
from unittest import result
import requests
from bs4 import BeautifulSoup


# url = "https://www.ss.lv/ru/transport/cars/alfa-romeo/"

# headers = {
#     "accept: */*",
#     "user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
# }
# result = requests.get(url)
# src = result.text
# # print(src)


# with open("scrap_sslv.html", "w", encoding="utf8") as  f:
#     f.write(src)



with open("scrap_sslv_2.html") as file:
     src = file.read()

soup = BeautifulSoup(src, "html.parser")
all_cars = soup.find(class_="msga2 pp0")
for cars in all_cars:
    print(cars)










# def get_html(url):
#     try:
#         result = requests.get(url) # при помощи reguests берем данные с этого url
#         result.raise_for_status() # для обработки исключений 
#         return result.text # если страница удачно скачена она будет внутри result.text
#     except(requests.RequestException, ValueError): # RequestException получим если какая то сетевая проблема, ValueError если на стороне сервера возникла какая то проблема
#         print("Сетевая ошибка")
#         return False



# def get_sslv_cars(html):
#     soup = BeautifulSoup(html, "html.parser") # теперь soup это будет html преобразованный в дерево в котором мы будем делать поиск
#     all_cars = soup.find(class_="msga2 pp0").find_parent() #теперь делаем поиск нужного нам дочернего элемента: тега и class  и захватывая весь блок движемся к родительскому тегу
#     result_cars = [] # создадим список
#     for cars in all_cars:                  # создадим цикл в котором пройдемся
#         result_cars.append(
#             {
#                 # id = cars.find("").text  # (integer)
#                 # print(id)
#                 "desccruption" : cars.find("dif").text     # описание (string)
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
#     return result_cars



# print(get_sslv_cars(html.text))



# if __name__ == "__main__":
#     html = get_html("https://www.ss.lv/ru/transport/cars/alfa-romeo/")
#     if html: 
#         # with open("scrap_sslv.html", "w", encoding="utf8") as  f: # мы открыли файл на запись 
#         #    f.write(html)  # и записываем в него наши данные из html
#         get_sslv_cars(html)
            



