import uuid


class Book:
    """Класс для представления книги."""

    def __init__(self, title: str, author: str, year: int, status: str = "в наличии"):
        self.id = str(uuid.uuid4())
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def to_dict(self) -> dict:
        """Возвращает данные книги в виде словаря."""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "status": self.status,
        }

    @staticmethod
    def from_dict(data: dict) -> "Book":
        """Создаёт экземпляр книги из словаря."""
        return Book(
            title=data["title"],
            author=data["author"],
            year=data["year"],
            status=data["status"],
        )


class Library:
    """Класс для управления библиотекой."""

    def __init__(self):
        self.books = []

    def add_book(self, book: Book) -> None:
        """Добавляет новую книгу в библиотеку."""
        self.books.append(book)

    def remove_book(self, book_id: str) -> bool:
        """Удаляет книгу по её ID."""
        for book in self.books:
            if book.id == book_id:
                self.books.remove(book)
                return True
        return False

    def find_books(self, field: str, value: str) -> list[Book]:
        """Ищет книги по указанному полю."""
        valid_fields = {"title", "author", "year"}  # Допустимые поля (без "status")
        if field not in valid_fields:
            raise ValueError(f"Поле '{field}' не существует. Допустимые поля: {', '.join(valid_fields)}.")

        results = []
        for book in self.books:
            book_value = getattr(book, field, None)
            if book_value is not None and str(book_value).lower() == value.lower():
                results.append(book)
        return results

    def update_status(self, book_id: str, new_status: str) -> bool:
        """Обновляет статус книги."""
        for book in self.books:
            if book.id == book_id:
                book.status = new_status
                return True
        return False
