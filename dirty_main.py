from datetime import *
from application.salary import *
from application.db.people import *

if __name__ == '__main__':
    print(f'Зарплатный фонд первого департамента: {calculate_salary(first_department)} по состоянию на {datetime.now()}')
    print(f'Сотрудники второго департамента: {get_employees(second_department)} по состоянию на {datetime.now()}')
