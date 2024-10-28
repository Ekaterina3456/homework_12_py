# Создайте класс Person, который имеет атрибуты name, age, и email. При
# установке значения атрибута name, оно должно начинаться с заглавной буквы.
# При установке значения атрибута age, оно должно быть целым числом в
# диапазоне от 0 до 120. При установке значения атрибута email, оно должно
# содержать символ @.

class Person:
    def __init__(self, name, age, email):
        self.name = name
        self.age = age
        self.email = email

    def __setattr__(self, key, value):
        if key == 'name':
            if not value[0].isupper() and not value.isalpha():
                raise ValueError('имя написано не с большой буквы либо в нём содержатся цифры')
        elif key == 'age':
            if not (isinstance(value, int) or value < 0 or value > 120):
                raise ValueError('возраст должен состоять только из чисел '
                                 'и быть в диапазоне от 0 до 120')
        elif key == 'email':
            if not '@' in value:
                raise ValueError('email должен содержать символ "@"')

    def __str__(self):
        return f'{self.name}, {self.age}, {self.email}'

if __name__ == '__main__':
    p1 = Person('reg', 153, 'esws@wge')
    # print(p1)
