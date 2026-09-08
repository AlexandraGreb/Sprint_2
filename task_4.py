class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name: str, hours: int = None, rest_days: int = 0, email: str = None):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name: str, hours: int = None, rest_days: int = 0, email: str = None):
        if hours is None:
            hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name: str, hours: int = None, rest_days: int = 0, email: str = None):
        if email is None:
            email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, new_rate: int):
        cls.hourly_payment = new_rate

    def salary(self):
        return self.hours * self.hourly_payment

emp1 = EmployeeSalary.get_hours(name="Игорь", rest_days=2, email="igor@main.ru")
print(f"Сотрудник: {emp1.name}, Часы: {emp1.hours}, Зарплата: {emp1.salary()}") 

emp2 = EmployeeSalary.get_email(name="Ольга", hours=35)
print(f"Сотрудник: {emp2.name}, Почта: {emp2.email}, Зарплата: {emp2.salary()}")
print("-" * 30)

EmployeeSalary.set_hourly_payment(600)

print(f"Новая зарплата {emp2.name}: {emp2.salary()}")
