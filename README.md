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
# Подготовка к запуску
1. Создайте в корневой папке файл с название `.env`
2. Сделайте там поля:
```sh
GOOGLE_CLIENT_ID=
GOOGLE_CLIENT_SECRET=
secret_key=
   ```
3. В командной строке или в отдельном файле Python запустите следующий набор команд:

```sh
python
```
```sh
import os
```
```sh
os.urandom(16)
```
4. Получившуюся строку, которая начинается с `b'`, вставьте после secret_key, чтобы получилось что-то такое:
   ```sh
   secret_key=b'...'
   ```
5. Получим остальные данные:
6. Перейдите по ссылке: https://console.cloud.google.com/projectselector2/apis/credentials
   - Если у вас нет проекта, нажмите на кнопку `Create project` на главном экране
   - Можете создать проект просто нажав на кнопку согласия без изменений
   - Если у вас есть проект, выберите его или создайте новый
7. Теперь вы на вкладке https://console.cloud.google.com/apis/credentials
8. В верхней части экрана нажмите на кнопку `+ CREATE CREDENTIALS`
   - OAUTH client ID
   - Если вам предлагают настроить экран согласия, пройдите по инструкции, которую предоставляет гугл (нажмите на кнопку `configure consent screen`)
   - Если вы прошли второй пункт 8., нажмите External и нажмите `create`
   - Заполните необходимые поля и при окончании настройки, вернитесь на пунке 7.
9. Выберите `Web application`
10. Укажите в Authorized redirect URI's:
    http://127.0.0.1:5000/dashboard и http://127.0.0.1:5000/login/google/authorized
11. Нажмите create
12. Теперь перед вами плашка с некоторыми значениями:
13. Client secret скопируйте и вставьте после `GOOGLE_CLIENT_SECRET=` в вашем .env файле
14. Client ID скопируйте и вставьте после `GOOGLE_CLIENT_ID=` в вашем .env файле
15. Ваш .env файл должен выглядеть примерно так:
    ```sh
    GOOGLE_CLIENT_ID=(...).apps.googleusercontent.com
    GOOGLE_CLIENT_SECRET=...
    secret_key=b'...'
    ```
16. Наш сайт готов к запуску! (Но перед запуском рекомендуем заново проделать пункты 3. и 4. )
# Запуск

1. Запустите приложение:
    ```sh
    python main.py
    ```

2. Откройте браузер и перейдите по адресу:
    ```
    http://127.0.0.1:5000/
    ```
> [!WARNING]
> Пожалуйста, не используйте http://localhost:5000/, используйте http://127.0.0.1:5000/
# Структура проекта

- [`main.py`](/main.py) - основной файл приложения Flask.
- [`templates`](/templates) - директория с HTML-шаблонами.
- [`static`](/static) - директория с файлами статики (CSS, JS, изображения).
- [`Samples_For_Courses`](/Samples_For_Courses/) - материалы курсов, предоставляемых на сайте
- [`requirements.txt`](/README.md) - список зависимостей проекта.

# Демонстрация работы сайта

Наш сайт "Сдай ЕГЭ" предоставляет множество возможностей для подготовки к ЕГЭ. Вы можете ознакомиться с функционалом сайта, просмотрев демонстрационное видео по следующей ссылке:

[Демонстрация работы сайта на vkVideo](https://vkvideo.ru/video519149335_456239531?list=ln-BQQCfTZp5Z6bg9pGLH)

В этом видео вы увидите:
- Как зарегистрироваться и войти на сайт.
- Как использовать фильтры для поиска заданий по сложности, типу и источнику.
- Как решать задания и проверять свои ответы.
- Как создавать и управлять группами для учителей.
- Как использовать готовые варианты для подготовки к экзамену.
- Как пользоваться форумом для общения с другими пользователями.

Мы надеемся, что это видео поможет вам лучше понять, как использовать наш сайт для подготовки к ЕГЭ.
