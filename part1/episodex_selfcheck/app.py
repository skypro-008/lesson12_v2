# Как отдать простую текстовую страничку?

# Чтобы отдать простую текстовую страничку, мы объявляем некую функцию,
# пишем по какому адресу она будет и пишем ретерн «текст странички».
#
# from flask import Flask
#
#
# app = Flask(__name__)
#
# @app.route("/")
# def page_index():
#     return "Hello world"
#

#
# Как нам запустить фласк?
# Чтобы нам запустить фласк, помимо всей вот этой конфигурации, есть два основных момента:
# создание, собственно, фласка, импорт, создание фласка, описание всех функций и апп.ран.
# Без этого ничего не заработает.
#
#
# app.run()


# Как получить переменную сегмента урл?
# Делается это с помощью треугольных скобочек <> и названия переменной,
# которое мы просто передаем в параметр нашего метода.
#
# @app.route("/profile/<int:uid>")
# def page_profile(uid):
#     return "Hello world"



# Как нам получить квери-параметр?
# Мы переходим к реквест.аргс и потом пытаемся получить.
# Если мы хотим, чтобы это было безопасно, чтобы ничего не падало то используем гет

# @app.route("/")
# def page_profile():
#     return request.args.get("username")

# Если мы точно уверены, что там это слово должно быть, то можем обратиться к обычному словарю,
# но тогда если вдруг этого параметра нет – у нас будет ошибка 500.
#
# @app.route("/")
# def page_profile():
#     return request.args["username"]



# Как обработать ошибку?
# Большинство ошибок фласк обрабатывает сам, но если мы хотим сделать какой-то дополнительный эррор хедлер,
# то делаем функцию с декоратором эроррхедлер.
#
#
# @app.errorhandler(404)
# def page_not_found(e):
# 	return "Страница не найдена", 404
#
# @app.errorhandler(500)
# def page_server_error(e):
# 	return "Ошибка на сервере", 500



# Ну и последнее. Как сделать редирект? С помощью функции редирект.
#
#
# from flask import Flask, redirect
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello():
#     return redirect("http://www.example.com", code=302)


