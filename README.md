## Условия
Задание 2.
Используя django/flask(на выбор), реализовать приложение, которое является агрегатором данных из access логов apache с сохранением в БД.
Разбор файлов должен выполняться по cron'у .

В приложении реализовать такие функции:
- авторизация (пользователи в БД)
- просмотр данных сохраненных в БД (группировка по IP, по дате, выборка по промежутку дат)
- API для получения данных в виде JSON (смысл тот же: получение данных по временному промежутку, возможность группировать/фильтровать по IP)
- конфигурация через файл настроек (где лежат логи, маска файлов, и все, что Вам потребуется для настройки приложения)

СУБД: mysql/postgresql

# Запуск

вап

# Пояснения
1. Перед запуском необходимо настроить configuration.ini - указать директорию откуда будут браться файлы логов 
для агрегатора по крону. 
2. Периодичность проверки и обработки логов установлена по дефолту - в 1 час.
Начал реализовывать функционал на сelery + celery-beat, но как выяснилось django-celery-beat отвалилась 
и не ставится на Django выше 4 версии. Можно было бы откатить версии и продолжить, но было принято решение 
создать новый велосипед :-))). 
Периодичность выполняется по кастомной команде, запускает ее шедулер [Ofelia](https://github.com/mcuadros/ofelia). 
Дальнейшая обработка файлов передается в задачи Dramatiq
