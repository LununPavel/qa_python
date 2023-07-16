import pytest
from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre_assign_genre_to_book(self):
        collector = BooksCollector()

        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')

        assert collector.get_books_genre() == {'Сияние': 'Ужасы'}


    def test_set_book_genre_assign_genre_to_book_thet_is_not_in_list(self):
        collector = BooksCollector()

        collector.add_new_book('Задача выжить')
        collector.set_book_genre('Задача выжить', 'Боевик')

        assert collector.get_book_genre('Задача выжить') == ''


    @pytest.mark.parametrize('book_name,book_genre', [
        ['Сияние', 'Ужасы'],
        ['Шаровая молния', 'Фантастика'],
        ['Шрек', 'Мультфильмы']
    ])
    def test_get_book_genre_(self, book_name, book_genre):
        collector = BooksCollector()

        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, book_genre)

        assert collector.get_book_genre(book_name) == book_genre


    def test_get_books_with_specific_genre_get_book_names_with_same_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_new_book('Шаровая молния')
        collector.set_book_genre('Шаровая молния', 'Фантастика')
        collector.add_new_book('Остров фантазий')
        collector.set_book_genre('Остров фантазий', 'Ужасы')


        assert collector.get_books_with_specific_genre('Ужасы') == ['Сияние', 'Остров фантазий']


    def test_get_books_with_specific_genre_get_empty_list_of_books(self):
        collector = BooksCollector()

        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_new_book('Шаровая молния')
        collector.set_book_genre('Шаровая молния', 'Фантастика')
        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')

        assert collector.get_books_with_specific_genre('Боевики') == []


    def test_get_books_genre_get_dict_books_genre(self):
        collector = BooksCollector()

        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_new_book('Шаровая молния')
        collector.set_book_genre('Шаровая молния', 'Фантастика')
        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')

        assert collector.get_books_genre() == {
            'Сияние': 'Ужасы',
            'Шаровая молния': 'Фантастика',
            'Шрек': 'Мультфильмы'
        }


    def test_get_books_for_children_get_list_of_children_books(self):
        collector = BooksCollector()

        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')
        collector.add_new_book('Горе от ума')
        collector.set_book_genre('Горе от ума', 'Комедии')
        collector.add_new_book('Последний гамбит')
        collector.set_book_genre('Последний гамбит', 'Детективы')
        collector.add_new_book('Шрек')
        collector.set_book_genre('Шрек', 'Мультфильмы')

        assert collector.get_books_for_children() == ['Горе от ума', 'Шрек']


    def test_add_book_in_favorites_add_three_books_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Бессмертие')
        collector.add_new_book('Ящик Скиннера')
        collector.add_new_book('Бессмертие')
        collector.add_new_book('Скрытые намерения')

        collector.add_book_in_favorites('Бессмертие')
        collector.add_book_in_favorites('Ящик Скиннера')
        collector.add_book_in_favorites('Бессмертие')
        collector.add_book_in_favorites('Скрытые намерения')
        collector.add_book_in_favorites('Большой круг')

        assert collector.get_list_of_favorites_books() == ['Бессмертие', 'Ящик Скиннера', 'Скрытые намерения']


    def test_delete_book_from_favorites_delete_one_favorite_books(self):
        collector = BooksCollector()

        collector.add_new_book('Бессмертие')
        collector.add_new_book('Ящик Скиннера')

        collector.add_book_in_favorites('Бессмертие')
        collector.add_book_in_favorites('Ящик Скиннера')

        collector.delete_book_from_favorites('Бессмертие')

        assert collector.get_list_of_favorites_books() == ['Ящик Скиннера']


    def test_get_list_of_favorites_books_get_list_of_two_selected_books(self):
        collector = BooksCollector()

        collector.add_new_book('Бессмертие')
        collector.add_new_book('Ящик Скиннера')

        collector.add_book_in_favorites('Бессмертие')
        collector.add_book_in_favorites('Ящик Скиннера')

        assert collector.get_list_of_favorites_books() == ['Бессмертие', 'Ящик Скиннера']
