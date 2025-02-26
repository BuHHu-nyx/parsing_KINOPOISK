from bs4 import BeautifulSoup
import requests
import pandas as pd
import time
def collect_user_rates(user_login):
   page_num = 1
   data = []
   while True:
       url = f'https://www.kinopoisk.ru/user/{user_login}/votes/list/vs/vote/page/{page_num}/#list'
       html_content = requests.get(url).text
       soup = BeautifulSoup(html_content, 'lxml')
       entries = soup.find('div', class_='profileFilmsList')
       if entries == None:
           print(f"Парсинг успешно выполнен, количество собранных страниц:{page_num}")# Признак остановки
           break
       film_details = entries.find_all('div', class_='item')
       for film in film_details:
           name = film.find('a').text
           film_name = name.split('(')[0]
           date = name.split('(')[1]
           release_date = date.split(')')[0]
           rating = film.find('div', class_='vote').text
           data.append({'film_name': film_name, 'release_date': release_date, 'rating': rating})
       page_num += 1
       time.sleep(10)
   return data
user_rates = collect_user_rates(user_login= '77483303')
df = pd.DataFrame(user_rates)
df.to_excel('user_rates.xlsx')