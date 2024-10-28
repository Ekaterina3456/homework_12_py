# Создайте класс Book, который создает экземпляры с помощью __new__. Убедитесь,
# что каждый экземпляр имеет уникальный идентификатор.

class Book:
    _id_counter = 1

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        instance.id = cls._id_counter
        cls._id_counter += 1
        return instance

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'book - {self.title}, author - {self.author}, id - {self.id}'


if __name__ == '__main__':
    b1 = Book('двойник', "жозе самораго")
    print(b1)
    b2 = Book('дом в котором', "неизвестно")
    print(b2)
