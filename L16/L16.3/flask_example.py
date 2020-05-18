from flask import Flask, request, render_template
app = Flask(__name__)


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


@app.route('/moto')
def motos():
    # model, price = 'BMW', 0.8
    # template_context = dict(model=model, price = price)
    # return render_template('moto.html', **template_context)
    data = {
        'model': 'BMV',
        'price': 0.8}
    return render_template('moto.html', **data)

if __name__ == "__main__":
    app.run(debug=True)

