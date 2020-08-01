import datetime
import csv
print("Time-Tracking Program\n")
print("Kindly enter your details by following the formats indicated\n")

# Parse the date values in format and parse work rate
s_date = input('Starting date in dd/mm/yyyy format: ')
s_time = input('Starting time in hh:mm 24hrs format: ')
sday, smonth, syear = map(int, s_date.split('/'))
shour, smin = map(int, s_time.split(':'))

f_date = input('Finishing date in dd/mm/yyyy format: ')
f_time = input('Finishing time in hh:mm 24hrs format: ')
fday, fmonth, fyear = map(int, f_date.split('/'))
fhour, fmin = map(int, f_time.split(':'))

start = datetime.datetime(syear, smonth, sday, shour, smin)
end = datetime.datetime(fyear, fmonth, fday, fhour, fmin)


# Calculate the time diff in hours. time diff = end - start
def calc_hours():
    time_diff = end - start
    return time_diff.total_seconds() / 3600


hours = calc_hours()


# Calcuate the income. income = time diff * hourly rate [Hourly rate = $5]
def calc_inc():
    inc = hours * 5

    return inc


income = calc_inc()

# write the details to csv file in the format : start date, end date, hourly rate and income
def main():
    details = [start, end, hours, income]
    with open('Income.csv', "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(details)


if __name__ == "__main__":
    main()

print("The number of hours worked is {:.2f} hours\n".format(hours))
print("The income earned is ${:.2f}\n".format(income))

print('Thank you for using our app\n')
input('Press the enter key to exit.')