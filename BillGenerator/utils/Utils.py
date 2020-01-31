from pathlib import Path
import calendar
import datetime
from random import randint


def getProjectDir():
    return Path(__file__).parent.parent.absolute()


def get_date():
    today = datetime.date.today()
    dates = ["2014-01-07", "2016-10-10"]


def generate_dates(fromDate, end, fineDate, billNumber):
    fromDate = datetime.datetime.strptime(fromDate, "%d-%b-%Y").date()
    billDate = end = datetime.datetime.strptime(end, "%d-%b-%Y").date()
    fineDate = datetime.datetime.strptime(fineDate, "%d-%b-%Y").date()
    dates = list()
    while True:
        if (billDate - end).days < 20:
            try:
                billDate = fromDate.replace(day=end.day, month=fromDate.month + 1)
                fineDate = fromDate.replace(day=fineDate.day, month=billDate.month + 1)
            except ValueError:
                if fromDate.month == 12:
                    billDate = fromDate.replace(day=end.day, year=fromDate.year + 1, month=1)
                    fineDate = fromDate.replace(day=fineDate.day, year=fromDate.year + 1, month=2)
                if fineDate.month == 12:
                    fineDate = fromDate.replace(day=fineDate.day, year=fromDate.year + 1, month=1)

            dates.append((fromDate.strftime("%d-%b-%Y"), billDate.strftime("%d-%b-%Y"), fineDate.strftime("%d-%b-%Y"),
                          generate_bill_number(billNumber)))
            fromDate = billDate.replace(day=fromDate.day)
        else:
            break
    return dates


def generate_bill_number(billNumber):
    no_of_times = randint(0, len(billNumber) - 1)
    for i in range(no_of_times):
        index = randint(0, len(billNumber) - 1)
        if index > 1:
            # return billNumber.replace(billNumber, str(randint(0, 9)))
            billNumber = '%s%s%s' % (billNumber[:index], str(randint(0, 9)), billNumber[index + 1:])
    return billNumber
