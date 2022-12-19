import requests
import pandas as pd
from bs4 import BeautifulSoup
import re

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

def get_financial_statements(code):
    # 인증값 추출
    re_enc = re.compile("encparam: '(.*)'", re.IGNORECASE)
    re_id = re.compile("id: '([a-zA-Z0-9]*)' ?", re.IGNORECASE)

    url = "https://companyinfo.stock.naver.com/v1/company/c1010001.aspx?cmp_cd={}".format(code)
    html = requests.get(url, verify=False).text

    search = re_enc.search(html)
    if search is None:
        return {}
    encparam = re_enc.search(html).group(1)
    encid = re_id.search(html).group(1)

    # 스크래핑
    url = "https://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?cmp_cd={}&fin_typ=0&freq_typ=A&encparam={}&id={}".format(
        code, encparam, encid)
    headers = {"Referer": "HACK"}
    html = requests.get(url, headers=headers, verify=False).text

    soup = BeautifulSoup(html, "html5lib")
    dividend = soup.select("table:nth-of-type(2) tr:nth-of-type(33) td span")
    years = soup.select("table:nth-of-type(2) th")

    dividend_dict = {}
    for i in range(len(dividend)):
        dividend_dict[years[i + 3].text.strip()[:4]] = dividend[i].text

    return dividend_dict

def get_dividend_yield(code):
    url = "http://companyinfo.stock.naver.com/company/c1010001.aspx?cmp_cd=" + code
    html = requests.get(url, verify=False).text

    soup = BeautifulSoup(html, 'html5lib')
    dt_data = soup.select("td dl dt")

    dividend_yield = dt_data[-2].text
    dividend_yield = dividend_yield.split(' ')[1]
    dividend_yield = dividend_yield[:-1]

    return dividend_yield

def get_estimated_dividend_yield(code):
    dividend_yield = get_financial_statements(code)
    dividend_yield = sorted(dividend_yield.items())[-1]
    return dividend_yield[1]

if __name__ == "__main__":
    print("dividend_dict \n ==============")
    dividend_dict = get_financial_statements("035720")
    print(dividend_dict)
    dividend_yield = get_dividend_yield('058470')
    #print(dividend_yield)
    print("==============\n==============")
    estimated_dividend_yield = get_estimated_dividend_yield('058470')
    print(estimated_dividend_yield)