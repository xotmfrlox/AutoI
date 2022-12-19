import datetime
import webreader
import sys
from PyQt5.QtWidgets import *

class PyMon:
    def get_min_max_dividend_to_treasury(self, code):
        previous_dividend_yield = webreader.get_previous_dividend_yield(code)
        three_years_treasury = webreader.get_3year_treasury()

        now = datetime.datetime.now()
        cur_year = now.year
        previous_dividend_to_treasury = {}

        for year in range(cur_year-5, cur_year):
            if year in previous_dividend_yield.keys() and year in three_years_treasury.keys():
                ratio = float(previous_dividend_yield[year]) / float(three_years_treasury[year])
                previous_dividend_to_treasury[year] = ratio

        #print(previous_dividend_to_treasury)
        if not previous_dividend_yield:
            return (0, 0)

        min_ratio = min(previous_dividend_to_treasury.values())
        max_ratio = max(previous_dividend_to_treasury.values())

        return (min_ratio, max_ratio)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    pymon = PyMon()
    print(pymon.get_min_max_dividend_to_treasury("005930"))