from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import csv
import time

# Указал путь к ChromeDriver
service = Service(r'C:\Users\Pavilion\PycharmProjects\yandex_analiz\chromedriver-win64\chromedriver.exe')

# Инициализировал драйвера
driver = webdriver.Chrome(service=service)

# Открытие веб-страницы
driver.get("https://yandex.kz/pogoda/month?lat=43.273564&lon=76.914851&via=hnav")
time.sleep(5)  # таймер, для загрузки страницы полностью

# Сбор данных
weather_data = []
days = driver.find_elements(By.CSS_SELECTOR, '.climate-calendar-day__day')
temps_day = driver.find_elements(By.CSS_SELECTOR, '.climate-calendar-day__temp-day .temp__value')
temps_night = driver.find_elements(By.CSS_SELECTOR, '.climate-calendar-day__temp-night .temp__value')

for day, temp_day, temp_night in zip(days, temps_day, temps_night):
    weather_data.append([day.text, temp_day.text, temp_night.text])

# Закрытие драйвера
driver.quit()

# Сохранение данных в CSV
with open('weather_data.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Day', 'Temperature Day', 'Temperature Night'])
    writer.writerows(weather_data)

print("Данные о погоде сохранены в 'weather_data.csv'")
