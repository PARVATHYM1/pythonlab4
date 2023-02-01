import time
import datetime
print("1.Current date and time: " , datetime.datetime.now())
print("2.Current year: ", datetime.date.today().strftime("%Y"))
print("3.Current date and time: " , datetime.date.today().strftime("%B"))
print("4.Week number of the year: ", datetime.date.today().strftime("%W"))
print("5.Weekday of the week: ", datetime.date.today().strftime("%w"))
print("6.Day of year: ", datetime.date.today().strftime("%j"))
print("7.Day of the month : ", datetime.date.today().strftime("%d"))
print("8.Day of week: ", datetime.date.today().strftime("%A"))