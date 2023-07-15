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
        assert len(collector.books_genre) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_set_book_genre_assign_genre_to_book(self):
        collector = BooksCollector()

        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')

        assert collector.books_genre == {'Сияние': 'Ужасы'}


    def test_set_book_genre_assign_genre_to_book_thet_is_not_in_list(self):
        collector = BooksCollector()

        collector.add_new_book('Задача выжить')
        collector.set_book_genre('Задача выжить', 'Боевик')

        assert collector.books_genre['Задача выжить'] == ''


    @pytest.mark.parametrize('book_name,book_genre', [
        ['Сияние', 'Ужасы'],
        ['Шаровая молния', 'Фантастика'],
        ['Шрек', 'Мультфильмы']
    ])
    def test_get_book_genre_(self, book_name, book_genre):
        collector = BooksCollector()

        collector.books_genre = {book_name: book_genre}

        assert collector.get_book_genre(book_name) == book_genre


    def test_get_books_with_specific_genre_get_book_names_with_same_genre(self):
        collector = BooksCollector()

        collector.books_genre = {
            'Сияние': 'Ужасы',
            'Шаровая молния': 'Фантастика',
            'Остров фантазий': 'Ужасы',
            'Шрек': 'Мультфильмы',
            'Солнцестояние': 'Ужасы'
        }
        assert collector.get_books_with_specific_genre('Ужасы') == ['Сияние', 'Остров фантазий', 'Солнцестояние']


    def test_get_books_with_specific_genre_get_empty_list_of_books(self):
        collector = BooksCollector()

        collector.books_genre = {
            'Сияние': 'Ужасы',
            'Шаровая молния': 'Фантастика',
            'Остров фантазий': 'Ужасы',
            'Шрек': 'Мультфильмы',
            'Солнцестояние': 'Ужасы'
        }
        assert collector.get_books_with_specific_genre('Боевики') == []


    def test_get_books_genre_get_dict_books_genre(self):
        collector = BooksCollector()

        dict_books = collector.books_genre = {
            'Сияние': 'Ужасы',
            'Шаровая молния': 'Фантастика',
            'Остров фантазий': 'Ужасы',
            'Шрек': 'Мультфильмы',
            'Солнцестояние': 'Ужасы'
        }
        assert dict_books == {
            'Сияние': 'Ужасы',
            'Шаровая молния': 'Фантастика',
            'Остров фантазий': 'Ужасы',
            'Шрек': 'Мультфильмы',
            'Солнцестояние': 'Ужасы'
        }


    def test_get_books_for_children_get_list_of_children_books(self):
        collector = BooksCollector()

        collector.books_genre = {
            'Сияние': 'Ужасы',
            'Горе от ума': 'Комедии',
            'Последний гамбит': 'Детективы',
            'Шрек': 'Мультфильмы',
            'Солнцестояние': 'Ужасы'
        }
        assert collector.get_books_for_children() == ['Горе от ума', 'Шрек']


    def test_add_book_in_favorites_add_three_books_in_favorites(self):
        collector = BooksCollector()

        collector.add_new_book('Бессмертие')
        collector.add_new_book('Ящик Скиннера')
        collector.add_new_book('Забытая девушка')
        collector.add_new_book('Бессмертие')
        collector.add_new_book('Скрытые намерения')

        for i in collector.books_genre:
            collector.add_book_in_favorites(i)

        assert collector.favorites == ['Бессмертие', 'Ящик Скиннера', 'Забытая девушка', 'Скрытые намерения']


    def test_delete_book_from_favorites_get_list_of_favorite_books(self):
        collector = BooksCollector()

        collector.favorites = ['Бессмертие', 'Ящик Скиннера', 'Забытая девушка', 'Скрытые намерения']
        collector.delete_book_from_favorites('Забытая девушка')

        assert collector.favorites == ['Бессмертие', 'Ящик Скиннера', 'Скрытые намерения']


    def test_get_list_of_favorites_books_get_list_of_two_selected_books(self):
        collector = BooksCollector()

        collector.favorites = ['Бессмертие','Забытая девушка', 'Скрытые намерения']
        collector.delete_book_from_favorites('Забытая девушка')

        assert collector.get_list_of_favorites_books() == ['Бессмертие', 'Скрытые намерения']
