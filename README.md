# Набор скриптов для работы с сервисом Evernote

## Общее описание

Данные набор скриптов обеспечивает взаимодействие с API Evernote

## Установка

Для работы скрипта необходим Python2, можно установить командой:
```commandline
sudo apt install python2
```
Или из пакетного менеджера ОС

Устанавливаем виртуальное окружение для Python2 командой:
```commandline
pip2 install virtualenv
```

Создаем виртуальное окружение командой:
```commandline
virtualenv -p /usr/bin/python2 env
```

Входим в виртуальное окружение командой:
```commandline
source env/bin/activate
```

## Настройка

Создайте файл `.env`  и заполните следующими параметрами:

`EVERNOTE_CONSUMER_KEY='Ваш ключ в Evernote` для получения регистрируемся [тут]('https://sandbox.evernote.com/Login.action?targetUrl=%2FHome.action%3F').

`EVERNOTE_CONSUMER_SECRET='Ваша секретная строка в Evernote` для получения регистрируемся [тут]('https://sandbox.evernote.com/Login.action?targetUrl=%2FHome.action%3F').

`EVERNOTE_PERSONAL_TOKEN='Ваш персональный TOKEN в Evernote` - процесс получения описан [тут]('https://dev.evernote.com/doc/articles/authentication.php').

`JOURNAL_TEMPLATE_NOTE_GUID='GUID заметки` - указываем GUID заметки, которая будет шаблоном (Необходимо предварительно создать).

`JOURNAL_NOTEBOOK_GUID='GUID вашего вашего блокнота` - Указываем GUID блокнота куда добавляем записи.

`INBOX_NOTEBOOK_GUID='GUID inbox вашего блокнота'`

## Запуск

- Скрипт `list_notebooks.py` выводит список ваших блокнотов (GUID и названия блокнотов). Запуск командой:
    ```commandline
    python list_notebooks.py
    ```

- Скрипт `add_note2journal.py` добавляет заметку в журнал по шаблону указанному в .env (JOURNAL_TEMPLATE_NOTE_GUID) . Запуск командой:
    ```commandline
    python add_note2journal.py YYYY-MM-DD
    ```

- Скрипт `dump_inbox.py` выводит записи из inbox вашего блокнота (INBOX_NOTEBOOK_GUID). Запуск командой:
    ```commandline
    python dump_inbox.py [number]
    ```

    Где number - не обязательный параметр указывающий на количество записей (по умолчанию 10 шт.)