from flask import Flask, render_template, request, redirect, url_for
import sqlite3
import random
app = Flask(__name__)



@app.route('/',  methods=['POST', 'GET'])
@app.route('/home/', methods=['POST', 'GET'])
def home():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    predict = cursor.execute("""SELECT * FROM predict """).fetchall()
    id = random.randint(0,16)
    predict1 = predict[id][1]
    return render_template('base.html', predict=predict, id=id, predict1=predict1)



@app.route('/service')
def service():
    return render_template('service.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/love')
def love():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    loves = cursor.execute("""SELECT * FROM cards WHERE title='Перевернута карта' """).fetchone()
    conn.close()
    return render_template('love.html', love=loves)

@app.route('/love_answer')
def love_answer():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    loves = cursor.execute("""SELECT * FROM cards """).fetchall()
    print(loves)
    conn.close()
    card = random.randint(0,11)
    return render_template('love_answer.html', love=loves, card=card)

@app.route('/future')
def future():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    futures = cursor.execute("""SELECT * FROM cards WHERE title='Перевернута карта' """).fetchone()
    conn.close()
    return render_template('future.html', future=futures)

@app.route('/future_answer')
def future_answer():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    futures = cursor.execute("""SELECT * FROM cards """).fetchall()
    conn.close()
    card = random.randint(0, 11)
    return render_template('future_answer.html', future=futures, card=card)

@app.route('/finances')
def finances():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    finances1 = cursor.execute("""SELECT * FROM cards WHERE title='Перевернута карта' """).fetchone()
    conn.close()
    return render_template('finances.html', finances=finances1)


@app.route('/finances_answer')
def finances_answer():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    finances1 = cursor.execute("""SELECT * FROM cards """).fetchall()
    conn.close()
    card = random.randint(0,11)
    return render_template('finances_answer.html', finances=finances1, card=card)

@app.route('/form/', methods=['POST', 'GET'])
def form():
    if request.method == "POST":
        name = request.form['name']
        phone = request.form['phone']
        problem = request.form['problem']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(''' INSERT INTO users (name, phone, problem)
                        VALUES(?,?,?)''', (name, phone, problem))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    return render_template('form.html')

@app.route('/shop_buy', methods=['POST', 'GET'])
def form_buy():
    if request.method == "POST":
        name = request.form['name']
        phone = request.form['phone']
        problem = request.form['problem']

        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute(''' INSERT INTO users (name, phone, problem)
                        VALUES(?,?,?)''', (name, phone, problem))
        conn.commit()
        conn.close()
        return redirect(url_for('shop'))
    return render_template('shop_buy.html')

@app.route('/shop')
def shop():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    products = cursor.execute("""SELECT * FROM shop""").fetchall()
    conn.close()
    return render_template('shop.html', products=products)


if __name__ == '__main__':
    app.run(debug=True)