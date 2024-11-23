import unittest
from models import Book, Library
from storage import load_books, save_books
import os


class TestLibrary(unittest.TestCase):
    def setUp(self):
        """Подготовка перед каждым тестом."""
        self.library = Library()
        self.test_file = "test_library.json"
        self.library.books = []  # Начинаем с пустой библиотеки

    def tearDown(self):
        """Очистка после каждого теста."""
        if os.path.exists(self.test_file):
            os.remove(self.test_file)

    def test_add_book(self):
        """Тест добавления книги в библиотеку."""
        book = Book("Война и мир", "Толстой", 1869)
        self.library.add_book(book)
        self.assertEqual(len(self.library.books), 1)
        self.assertEqual(self.library.books[0].title, "Война и мир")

    def test_remove_book(self):
        """Тест удаления книги из библиотеки."""
        book = Book("Война и мир", "Толстой", 1869)
        self.library.add_book(book)
        self.library.remove_book(book.id)
        self.assertEqual(len(self.library.books), 0)

    def test_find_books_by_title(self):
        """Тест поиска книги по названию."""
        book1 = Book("Война и мир", "Толстой", 1869)
        book2 = Book("Анна Каренина", "Толстой", 1877)
        self.library.add_book(book1)
        self.library.add_book(book2)

        results = self.library.find_books("title", "Война и мир")
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0].author, "Толстой")

    def test_find_books_by_author(self):
        """Тест поиска книги по автору."""
        book1 = Book("Война и мир", "Толстой", 1869)
        book2 = Book("Анна Каренина", "Толстой", 1877)
        book3 = Book("Преступление и наказание", "Достоевский", 1866)

        self.library.add_book(book1)
        self.library.add_book(book2)
        self.library.add_book(book3)

        results = self.library.find_books("author", "Толстой")
        self.assertEqual(len(results), 2)

    def test_update_status(self):
        """Тест изменения статуса книги."""
        book = Book("Война и мир", "Толстой", 1869)
        self.library.add_book(book)
        self.library.update_status(book.id, "выдана")

        self.assertEqual(self.library.books[0].status, "выдана")

    def test_save_and_load_books(self):
        """Тест сохранения и загрузки книг."""
        book1 = Book("Война и мир", "Толстой", 1869)
        book2 = Book("Анна Каренина", "Толстой", 1877)

        self.library.add_book(book1)
        self.library.add_book(book2)

        # Сохраняем книги
        save_books(self.library.books, self.test_file)

        # Загружаем книги
        loaded_books = load_books(self.test_file)
        self.assertEqual(len(loaded_books), 2)
        self.assertEqual(loaded_books[0].title, "Война и мир")
        self.assertEqual(loaded_books[1].title, "Анна Каренина")


if __name__ == "__main__":
    unittest.main()
