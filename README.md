# test_note
Привет! Меня зовут Марина. Представляю свое простое приложение для создания заметок.

Приложение напиcано на python с помощью Django.
Итак, в первую очередь я описала модели нашего юзера и заметок.
Создала миграции, но применить их в postgres не смогла, ошибка: relation "django_session" does not exist, 
хотя все настройки были сделаны верно. 
После 4-х часов мытарства решила работать на sqlite3 и -О ЧУДО!- миграции применились и я смогла работать дальше.
Написала views на создани заметки, вывода всех заметок, вывода одной заметки, а также для редактирования и удаления заметки.
К этим views описала сериализаторы.
Прописала urls.
Добавила ImageView, теперь к заметке можно загрузить картинку!
К сожалению, не смогла реализовать идеи для улучшения(замена шрифта и выделение текста), 
возможно, это больше относится к фронтэнду.
Заметки добавляла через djangoadmin, для этого создала superuser.
Вот его данные: username - mar.la, password - 123.
Также все посмотрела в Postman.
Спасибо за уделенное внимание!
