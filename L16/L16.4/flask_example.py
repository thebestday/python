from flask import Flask, request, render_template
app = Flask(__name__)

# ОБСУДИМ ПЕРЕДАЧУ ДАННЫХ ИЗ ФОРМЫ а так же методы get и post при использовании рендеринга шаблонов
# как правило отправляем данные методом post на сервер
# сервер принимает данные обрабатывает согласно лоигике сервра и дает ответ
# данные из формы с одного html документа можно отправить на другой html докумнент и там их использовать


@app.route('/')
@app.route('/main')
def hello():
    return render_template('main.html')


@app.route('/cars')
def cars():
    data = {
        'model': 'Volvo',
        'price': 1.5}
    return render_template('cars.html', data=data)



# ДОБАВИМ ОБРАБОТКУ ДЛЯ СТРАНИЦЫ cars_form и указем метод post И БУДЕМ ПЕРЕДАВАТЬ ДАННЫЕ ИЗ ФОРМЫ
@app.route('/cars_form', methods = ['POST'])
def cars_form():
    # получим данные из формы и выведем их на экран
    brand = request.form['brand']
    price = request.form['price']
    # print(brand, price)
    data = {
        'model': brand,
        'price': price}
    return render_template('cars_form.html', data=data)



@app.route('/moto')
def motos():
    # model, price = 'BMW', 0.8
    # template_context = dict(model=model, price = price)
    # return render_template('moto.html', **template_context)
    data = {
        'model': 'BMV',
        'price': 0.8}
    return render_template('moto.html', **data)



# # ПРОСТЕЙШАЯ Ф-Я ПО ПОЛУЧЕНИЮ ДАННЫХ (оба метода и get и post будут обрабатываться одной и той же функций index) из формы
# @app.route('/', methods=['GET', 'POST'])
# def index():
#     data = request.form['input_name']            # принимаем данные из формы и по ключу input_name (из формы может придти много данных) мы принимаем только один котрый под ключем input_name
#                                                 # и можем дальше уже что-либо делать с data




if __name__ == "__main__":
    app.run(debug=True)

