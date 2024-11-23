# Управление библиотекой книг

**Консольное приложение для управления библиотекой книг**.<br/>
Позволяет добавлять, удалять, искать и отображать книги.

---

## **Функционал**

### Основные возможности:
1. **Добавление книги**:
   - Пользователь вводит название, автора и год издания.
   - Книга добавляется в библиотеку с уникальным ID и статусом "в наличии".
   
2. **Удаление книги**:
   - Удаление книги по её уникальному идентификатору (ID).

3. **Поиск книги**:
   - Поиск книг по полям:
     - Название
     - Автор
     - Год издания

4. **Отображение всех книг**:
   - Выводит список всех книг в библиотеке, включая их ID, название, автора, год издания и статус.

5. **Изменение статуса книги**:
   - Пользователь может изменить статус книги на "в наличии" или "выдана".

6. **Сохранение и загрузка**:
   - Данные о книгах хранятся в JSON-файле (`library.json`), который создаётся автоматически.


### Установка
1. Клонируйте репозиторий:
```
git clone git@github.com:AleksandrKosmylev/library_manager.git
```
2. Перейдите в папку проекта:
```
cd library_manager/
```
3. Запустить приложение
```
python3 library_manager.py
```