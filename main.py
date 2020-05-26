from datetime import datetime
from application.salary import calculate_salary
from application.salary import get_employees
from application.db import people

if __name__ == '__main__':
    print(f'Зарплатный фонд первого департамента: {calculate_salary(people.first_department)} по состоянию на {datetime.now()}')
    print(f'Сотрудники второго департамента: {get_employees(people.second_department)} по состоянию на {datetime.now()}')
