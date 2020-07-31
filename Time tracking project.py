# Parse the date values in format and parse work rate
# Calculate the time diff in hours. time diff = end date - start date
# Calcuate the income. income = time diff * hourly rate
# write the details to csv file in the format : start date, end date, hourly rate and income

import datetime
import csv

def calculate_hours(start, end):
    start_date = datetime.datetime.strptime(start, '%b %d %Y %I:%M%p')
    end_date = datetime.datetime.strptime(end, '%b %d %Y %I:%M%p')

    time_diff = end_date - start_date

    return time_diff.total_seconds() / 3600

def calculate_income(hours, rate):
    income = hours * rate
    
    return income

def main():
    start_date = 'Jun 28 2018 9:00AM'
    end_date = 'Jun 28 2018 5:00PM'
    hourly_rate = 5

    time_diff = calculate_hours(start_date, end_date)
    income = calculate_income(time_diff, hourly_rate)

    details = [start_date, end_date, hourly_rate, income]

    with open('income.csv', "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(details)

if __name__ == "__main__":
    main()
