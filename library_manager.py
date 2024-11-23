import sys
from models import Book, Library
from storage import load_books, save_books
import locale

# Установка кодировки ввода/вывода в зависимости от системы
encoding = locale.getpreferredencoding()
sys.stdin = open(sys.stdin.fileno(), mode='r', encoding=encoding, buffering=1)
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding=encoding, buffering=1)


def main():
    """Основное меню приложения."""
    storage_file = "library.json"
    library = Library()
    library.books = load_books(storage_file)

    while True:
        print("\nМеню:")
        print("1. Добавить книгу")
        print("2. Удалить книгу")
        print("3. Найти книгу")
        print("4. Отобразить все книги")
        print("5. Изменить статус книги")
        print("6. Выход")

        choice = input("Выберите действие: ")

        if choice == "1":
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            try:
                year = int(input("Введите год издания книги: "))
                new_book = Book(title, author, year)
                library.add_book(new_book)
                save_books(library.books, storage_file)
                print(f"Книга '{title}' успешно добавлена!")
            except ValueError:
                print("Ошибка: Год издания должен быть числом.")
        elif choice == "2":
            book_id = input("Введите ID книги для удаления: ")
            if library.remove_book(book_id):
                save_books(library.books, storage_file)
                print(f"Книга с ID {book_id} удалена.")
            else:
                print(f"Книга с ID {book_id} не найдена.")
        elif choice == "3":
            try:
                field = input("Введите поле для поиска (название, автор, год): ").strip().lower()

                # Преобразование русских названий полей в их программные аналоги
                field_mapping = {
                    "название": "title",
                    "автор": "author",
                    "год": "year"
                }

                if field not in field_mapping:
                    raise ValueError("Поле для поиска указано неверно. Допустимые поля: название, автор, год.")

                field = field_mapping[field]  # Преобразуем в нужное поле
                value = input("Введите значение для поиска: ").strip()

                results = library.find_books(field, value)
                if results:
                    print("Найденные книги:")
                    for book in results:
                        print(book.to_dict())
                else:
                    print(f"Книги с {field} = '{value}' не найдены.")
            except ValueError as e:
                print(f"Ошибка: {e}")


        elif choice == "4":
            if library.books:
                print("Список книг:")
                for book in library.books:
                    print(book.to_dict())
            else:
                print("Библиотека пуста.")
        elif choice == "5":
            book_id = input("Введите ID книги для изменения статуса: ")
            new_status = input("Введите новый статус (в наличии/выдана): ")
            if new_status in ["в наличии", "выдана"]:
                if library.update_status(book_id, new_status):
                    save_books(library.books, storage_file)
                    print(f"Статус книги с ID {book_id} обновлён на '{new_status}'.")
                else:
                    print(f"Книга с ID {book_id} не найдена.")
            else:
                print("Ошибка: Недопустимый статус.")
        elif choice == "6":
            print("Выход из программы.")
            break
        else:
            print("Ошибка: Некорректный выбор.")


if __name__ == "__main__":
    main()
