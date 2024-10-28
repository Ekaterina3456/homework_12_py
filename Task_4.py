# Создайте класс Product с атрибутами name, price, и quantity. price должен
# быть положительным числом, а quantity неотрицательным целым числом. При
# попытке установить price или quantity, должен производиться контроль
# значений.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __setattr__(self, key, value):
        if key == 'price':
            if not value > 0:
                raise ValueError('цена не может быть отрицательной')
        elif key == 'quantity':
            if not (value > 0 or isinstance(value, int)):
                raise ValueError('количество должно быть целочисленным и больше 0')

    def __str__(self):
        return f'Product(name = {self.name}, цена - {self.price}, кольчество - {self.quantity})'

if __name__ == '__main__':
    p1 = Product('дыня', 97, 34)
    print(p1)
