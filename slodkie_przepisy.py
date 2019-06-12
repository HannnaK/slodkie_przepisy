from flask import Flask, render_template, request, get_flashed_messages
from slodkie_przepisy_funkcje import get_connection
from slodkie_przepisy_logowanie import auth_bp
from slodkie_przepisy_dodawanie import dodaj_bp
from slodkie_przepisy_usuwanie import usun_bp
from slodkie_przepisy_ciasta_kremy import przepis_bp

app = Flask(__name__)
app.secret_key = 'tajny-klucz-9523'
app.register_blueprint(auth_bp)
app.register_blueprint(dodaj_bp)
app.register_blueprint(usun_bp)
app.register_blueprint(przepis_bp)


@app.route('/')
def index():
    messages = get_flashed_messages()
    return render_template('index.html', messages=messages)


@app.route('/wyszukiwanie')
def szukany_przepis():
    conn = get_connection()
    c = conn.cursor()

    zapytanie = """
    SELECT * FROM ciasta WHERE nazwa LIKE ? 
    """

    fraza = request.args.get('fraza')
    fraza = f'%{fraza}%'

    c.execute(zapytanie, (fraza,))
    przepisy = []
    for linia in c:
        przepisy.append(linia)

    conn.close()

    return render_template('wyszukiwanie.html', przepisy=przepisy)


if __name__ == '__main__':
    app.run(debug=True)
