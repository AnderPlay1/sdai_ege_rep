# Описание проекта

Проект "Сдай ЕГЭ" предназначен для помощи учащимся в подготовке к ЕГЭ и учителям, которые хотят использовать данный сайт для помощи учащимся в этом. Сайт предоставляет различные задания, которые можно фильтровать по сложности, типу и источнику. На данном сайте предусмотрены группы для работы с преподавателями, курсы с необходимой для подготовки теорией и варианты для тестирования собственных сил, подготовленные редакцией нашего сайта.

# Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/AnderPlay1/sdai_ege_rep.git
    ```

2. Перейдите в директорию проекта:
    ```sh
    cd sdai_ege_rep
    ```

3. Создайте виртуальное окружение:
    ```sh
    python -m venv venv
    ```

4. Активируйте виртуальное окружение:
    - Windows:
        ```sh
        venv\Scripts\activate
        ```
    - macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

5. Установите зависимости:
    ```sh
    pip install -r requirements.txt
    ```

# Запуск

1. Запустите приложение:
    ```sh
    python main.py
    ```

2. Откройте браузер и перейдите по адресу:
    ```
    http://127.0.0.1:5000/
    ```

# Структура проекта

- [`main.py`](/main.py) - основной файл приложения Flask.
- [`templates`](/templates) - директория с HTML-шаблонами.
- [`static`](/static) - директория с файлами статики (CSS, JS, изображения).
- [`Samples_For_Courses`](/Samples_For_Courses/) - материалы курсов, предоставляемых на сайте
- [`requirements.txt`](/README.md) - список зависимостей проекта.

# Демонстрация работы сайта

Наш сайт "Сдай ЕГЭ" предоставляет множество возможностей для подготовки к ЕГЭ. Вы можете ознакомиться с функционалом сайта, просмотрев демонстрационное видео по следующей ссылке:

[Демонстрация работы сайта на vkVideo](https://vkvideo.ru/video519149335_456239530?list=ln-lzNXNcOKS5CIqzY9GG)

В этом видео вы увидите:
- Как зарегистрироваться и войти на сайт.
- Как использовать фильтры для поиска заданий по сложности, типу и источнику.
- Как решать задания и проверять свои ответы.
- Как создавать и управлять группами для учителей.
- Как использовать готовые варианты для подготовки к экзамену.
- Как пользоваться форумом для общения с другими пользователями.

Мы надеемся, что это видео поможет вам лучше понять, как использовать наш сайт для подготовки к ЕГЭ.
