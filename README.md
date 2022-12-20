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
### Day 1~4구
2022년 12월 19일 기준 구현 완료
[참고사진]
![image](https://user-images.githubusercontent.com/53934772/208352706-c9650698-f02b-4a07-b5dd-aca67253bbb9.png)

### - Day5
구현중
급등주 포착 알고리즘 실행시 과도한 트래픽 발생시 Kiwoom 증권에서 막는 현상 발생
![image](https://user-images.githubusercontent.com/53934772/208564669-cd53df27-e520-43be-8a3d-4db5849ce332.png)

### - Day6
min_ratio = min(previous_dividend_to_treasury.values())
ValueError: min() arg is an empty sequence
