# AutoI

## Mission Statements
#### AutoI는 **N잡러**를 지지합니다.
집을 사는 그날까지 **N잡러**의 시간이 되어드리겠습니다.

## 필요성
현재 30대미만이 서울의 아파트(10억4299만원)을 구매하기까지 **94.91**이 걸린다.
(3533만원(경상소득) – 1939만원(가계운영비등 소비) – 495만원(세금 등)  -> 1099만원 10억4299(서울아파트) / 1099만원)

즉 저축만으로 집을 사는게 불가능하기 때문에 근로소득 말고 별도의 소득이 필요하다.
하지만 주식은 많은 변수를 가지고 있기 때문에 수많은 알고리즘으로 예측할 수 있는 AutoI가 필요하다.

## 예상 UI
![image](https://user-images.githubusercontent.com/53934772/208350516-2fe4f253-2a26-45a9-a233-f1e602c74fe2.png)

## 사용 스택
- Language : Python
- UI : QT Designer
- DB : SQLite
- API : 키움 OpenAPPI+
- Tool : Pycharm

## 기능
- 자동 로그인
- 주문 기능
- 계좌 연동 후 잔고 및 종목 현황 출력
- 작성된 리스트로 주식 자동 주문
- 다양한 알고리즘
-> 급등주 포착, 기업 실적 데이터 바탕, 배당률 기반 투자 알고리즘 등

## Team
혼자 구현.
파이썬으로 배우는 알고리즘 트레이딩과 키움 OPEN API+ 설명서 참고

## 개발 일지
#### - Day1
자동 로그인, QT Designer로 윈도우창 생성 구현 완료
#### - Day2
주문 기능 추가 구현 완료
#### - Day3
주식 종목 현황 출력과 잔고확인 기능 구현 완료
#### - Day4
작성된 매수, 매도 리스트를 자동 주문 구현 완료
#### - Day5
급등주 포착 알고리즘 구현 예정
#### - Day6
기업 실적 데이터 바탕, 배당률 기반 투자 알고리즘 개발 예정

## 상세 설명

## Day 1~4
### [파이썬 구축]
**- 에러**
Failed to create a virtual environment
**- 원인**
파이썬 및 파이참 첫 설치 후 가상 머신이 설치되어있지 않아서 발생하는 에러
**- 해결 완료**
pip install virtualenv
python -m venv venv

**- 에러**
Could not fetch URL https://pypi.org/simple/pip/: There was a problem confirming the ssl certificate: HTTPSConnectionPool(host='pypi.org', port=443): Ma
x retries exceeded with url: /simple/pip/ (Caused by SSLError("Can't connect to HTTPS URL because the SSL module is not available.")) - skipping        
**- 해결**
환경변수 추가
C:\seulgi\it\language\python\Python\Anaconda3\Library\mingw-w64\bin
C:\seulgi\it\language\python\Python\Anaconda3\Library\bin

**- 에러**
Invalid Python SDK
**- 해결**
별도의 조치 없이 OK를 선택하니 작동됨

**- 에러**
Unresolved reference 'print'
**- 해결**
Invalidate and Restart 함


### [Kiwoom API 사용]
**- 에러**
SignKorea 인증서 부재 확인
이미 SignKorea 인증서를 발급 받은 사실이 있으나 현재 이용하는 PC내에 인증서가 존재하지 않거나 검색에 실패함.
**- 에러해결**
SignKorea에서 인증서 연장 후 키움증권에서 다시 인증서 발급함.

### [개발 에러]
**- 에러**
OpenSSL.SSL.Error: [('SSL routines', 'tls_process_server_certificate', 'certificate verify failed')]
**- 해결**
verify=False를 추가한다.

**- 에러(warning)**
InsecureRequestWarning: Unverified HTTPS request is being made. Adding certificate verification is strongly advised. See: https://urllib3.readthedocs.io/en/latest/advanced-usage.html#ssl-warnings
InsecureRequestWarning)
**- 해결**
warning이라 무시해도 되지만 신경 쓰이면 아래 문구를 추가해준다.
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

**- 에러**
ValueError: could not convert string to float: '15,242,370'
**- 원인**
'15,242,370'를 float형으로 바꾸지 못하는 에러
“,”가 빠지면 str형식을 float 형식으로 잘 변경된다.
기존 소스코드
replace 메서드를 이용해서 ,를 빼고 float형식으로 형변환을 실행한다.
estimated_dividend_to_treasury = float(estimated_dividend_yield) / float(current_3year_treasury)

변경 소스코드
estimated_dividend_yield = get_estimated_dividend_yield("058470")
    print("estimated_dividend_yield : " + estimated_dividend_yield)
    re_estimated_dividend_yield = estimated_dividend_yield.replace(",","")
    current_3year_treasury = get_current_3year_treasury()
    print("current_3year_treasury : " + current_3year_treasury)
    estimated_dividend_to_treasury = float(re_estimated_dividend_yield) / float(current_3year_treasury)
    print(estimated_dividend_to_treasury)

**2022년 12월 19일 기준 구현 완료**
[참고사진]
![image](https://user-images.githubusercontent.com/53934772/208352706-c9650698-f02b-4a07-b5dd-aca67253bbb9.png)

### - Day5
구현중
급등주 포착 알고리즘 실행시 과도한 트래픽 발생시 Kiwoom 증권에서 막는 현상 발생
![image](https://user-images.githubusercontent.com/53934772/208564669-cd53df27-e520-43be-8a3d-4db5849ce332.png)

### - Day6
min_ratio = min(previous_dividend_to_treasury.values())
ValueError: min() arg is an empty sequence
