class Cat:
    def __init__(self, name, sex, age):
        self.name = name
        self.sex = sex
        self.age = 0
        self.set_age(age)

    def set_age(self, value):
        if isinstance(value, int):
            self.age = int(value) if value <= 25 else 0

    def get_age(self):
        return self.age if self.age > 0 else 'Не определено'

    def get_information(self):
        return f'Кличка: {self.name} | Пол: {self.sex} | Возраст: {self.get_age()}'
