# 5분마다 한 번씩 서울의 기온 정보를 csv 형태로 저장!!
import requests
import csv
from datetime import datetime
import os

MY_API_KEY = os.getenv("OPENWEATHER_API_KEY")
city_name = "Seoul"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={MY_API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()
# 서울 기온
temp = data["main"]["temp"]
time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
csv_filename = "seoul_weather.csv"
header = ["time", "temp"]

# "seoul_weather.csv"가 없으면 새로 생성!!
# 만약 있다면, 갱신!!
file_exist = os.path.isfile(csv_filename)

# a mode : 없으면 write, 있으면 덮어쓰기
# w mode : 무조건 덮어쓰기
with open(csv_filename, "a", newline="") as file: # 개행옵션 off함
    writer = csv.writer(file)

    # 만약 csv가 없었다면
    # 헤더도 없다!!
    if not file_exist:
        writer.writerow(header)
    
    writer.writerow([temp, time])

    print("서울 기온 저장 완료!")

