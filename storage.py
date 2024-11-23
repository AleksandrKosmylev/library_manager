import json
from models import Book


def load_books(file_path: str) -> list[Book]:
    """Загружает книги из JSON файла."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:  # Явно указываем кодировку
            data = json.load(file)
            return [Book.from_dict(book) for book in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_books(books: list[Book], file_path: str) -> None:
    """Сохраняет книги в JSON файл."""
    with open(file_path, "w", encoding="utf-8") as file:  # Явно указываем кодировку
        json.dump([book.to_dict() for book in books], file, indent=4, ensure_ascii=False)
