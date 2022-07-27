from application.people import get_employees
from application.salary import calculate_salary
from datetime import datetime


def date_output():
    print(datetime.now())



def main():
    date_output()
    get_employees()
    calculate_salary()


if __name__ == '__main__':
    main()
