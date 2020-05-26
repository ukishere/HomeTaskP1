def calculate_salary(department):
    salary = 0
    for person in department:
        salary += person['salary']
    return salary

def get_employees(department):
    employees = [person['name'] for person in department]
    return employees