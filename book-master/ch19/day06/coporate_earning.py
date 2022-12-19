# 최근 5년에 대한 국채시가배당률 중 최댓값과 최솟값을 반환하는 함수 구현
# -> 최근 5년간 국채시가배당률의 최대값과 최솟값

import requests
import pandas as pd
from bs4 import BeautifulSoup
import webreader
import datetime
import time

url = "http://www.index.go.kr/strata/jsp/showStblGams3.jsp?stts_cd=288401&amp;idx_cd=2884&amp;freq=Y&amp;period=1998:2018"
html = requests.get(url, verify=False).text
soup = BeautifulSoup(html, 'html5lib')
td_data = soup.select("tr td")
print(td_data)

treasury_3year = {}
start_year = 1998

for x in td_data:
    treasury_3year[start_year] = x.text
    start_year += 1

    print(x)

previous_dividend_yield = webreader.get_previous_dividend_yield('058470')
print(previous_dividend_yield)
three_years_treasury = webreader.get_3year_treasury()
print(three_years_treasury)

now = datetime.datetime.now()
cur_year = now.year
previous_dividend_to_treasury = {}
print(now)
print(cur_year)


print(previous_dividend_yield.keys())
print(three_years_treasury.keys())

print("=======================================")

# previous_dividend_yield[year]과 hree_years_treasury[2017]를 가져오지 못함.
print(previous_dividend_yield[2017])
print(three_years_treasury[2017])