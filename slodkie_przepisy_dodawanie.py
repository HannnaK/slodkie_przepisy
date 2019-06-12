from flask import Blueprint, request, render_template, redirect, request, get_flashed_messages, flash
import sqlite3
from slodkie_przepisy_funkcje import get_connection, wszystkie_przepisy, wszystkie_kremy, wszystkie_skladniki, \
    wszystkie_zdjecia

from slodkie_przepisy_logowanie import login_required

dodaj_bp = Blueprint('dodaj_endpoints', __name__)


@dodaj_bp.route('/dodanie', endpoint='dodaj_przepis')
@login_required
def dodaj_przepis():
    return render_template('dodaj_przepis.html')


@dodaj_bp.route('/dodanie_ciasta', methods=['GET', 'POST'], endpoint='dodaj_ciasto')
@login_required
def dodaj_ciasto():
    if request.method == 'GET':
        messages = get_flashed_messages()
        opis_pola = 'Dodaj nowe ciasto lub ciasteczka: '
        pole = 'ciasto'
        pole2 = 'ciasteczka'
        lista_kremow = wszystkie_kremy()
        zdjecia = wszystkie_zdjecia()
        context = {'opis_pola': opis_pola, 'pole': pole, 'pole2': pole2, 'lista_kremow': lista_kremow,
                   'zdjecia': zdjecia, 'messages': messages}
        return render_template('dodaj_ciasto_krem.html', **context)

    if request.method == 'POST':

        nazwa = request.form['nazwa']
        rodzaj = request.form['rodzaj']
        przygotowanie = request.form['przygotowanie']
        id_k = request.form['id_k']
        nr_zdjecia = request.form['nr_zdjecia']

        if nazwa and przygotowanie:
            conn = get_connection()
            c = conn.cursor()

            conn.commit()

            zapytanie = """
            INSERT INTO "ciasta" ("nazwa", "rodzaj", "przygotowanie", "id_k", "nr_zdjecia") VALUES (?, ?, ?, ?, ?)
            """
            parametry = (nazwa, rodzaj, przygotowanie, id_k, nr_zdjecia)

            c.execute(zapytanie, parametry)

            conn.commit()
            conn.close()

            return redirect('/dodanie_skladnika_c')

        flash('Pola "Podaj nazwę", "Wybierz rodzaj" i "Podaj opis przygotowania" nie mogą być puste!')
        return redirect('/dodanie_ciasta')



@dodaj_bp.route('/dodanie_krem', methods=['GET', 'POST'], endpoint='dodaj_krem')
@login_required
def dodaj_krem():
    if request.method == 'GET':
        messages = get_flashed_messages()
        opis_pola = 'Dodaj nowy krem lub polewę: '
        pole = 'krem'
        pole2 = 'polewa'
        context = {'opis_pola': opis_pola, 'pole': pole, 'pole2': pole2, 'messages': messages}
        return render_template('dodaj_ciasto_krem.html', **context)

    if request.method == 'POST':
        nazwa = request.form['nazwa']
        rodzaj = request.form['rodzaj']
        przygotowanie = request.form['przygotowanie']

        if nazwa and przygotowanie:
            conn = get_connection()
            c = conn.cursor()

            zapytanie = """
            INSERT INTO "kremy" ("nazwa", "rodzaj", "przygotowanie") VALUES (?, ?, ?)
            """
            parametry = (nazwa, rodzaj, przygotowanie)

            c.execute(zapytanie, parametry)
            conn.commit()
            conn.close()

            return redirect('/dodanie_skladnika_k')
        flash('Uzupełnij wszystkie pola!')
        return redirect('/dodanie_krem')


@dodaj_bp.route('/dodanie_skladnika_c', methods=['GET', 'POST'], endpoint='dodaj_skladniki_c')
@login_required
def dodaj_skladniki_c():
    if request.method == 'GET':
        messages = get_flashed_messages()
        opis_pola = 'Dodaj składnik do ciasta/ciasteczek:'
        opis_pola_2 = 'Wybierz ciasto/ciasteczka: '
        lista_przepisow = wszystkie_przepisy()
        lista_skladnikow = wszystkie_skladniki()

        context = {'opis_pola': opis_pola, 'opis_pola_2': opis_pola_2, 'lista': lista_przepisow,
                   'lista_skladnikow': lista_skladnikow, 'messages': messages}
        return render_template('dodaj_skladniki.html', **context)

    if request.method == 'POST':
        id_c = request.form['id']
        id_skl_c = request.form['id_skl']
        ilosc_skl_c = request.form['ilosc_skl']

        if id_skl_c and ilosc_skl_c:
            conn = sqlite3.connect('baza.db')
            c = conn.cursor()
            c2 = conn.cursor()
            zapytanie = """
            INSERT INTO "ciasta_do_skladniki" ("id_c", "id_skl_c", "ilosc_skl_c") VALUES (?, ?, ?)
            """
            parametry = (id_c, id_skl_c, ilosc_skl_c)
            c.execute(zapytanie, (parametry))
            conn.commit()

            opis_pola = 'Do ciasta/ciasteczek są dodane następujące składniki: '

            zapytanie_2 = """
            SELECT s.skladnik FROM "ciasta" AS c
            LEFT JOIN "ciasta_do_skladniki" AS cds 
            ON c.id=cds.id_c
            LEFT JOIN "skladniki" AS s
            ON cds.id_skl_c=s.id
            WHERE c.id = ?
            """
            ciasto = 'ciasto'
            c2.execute(zapytanie_2, (id_c,))
            dodane_skldniki = [list(el) for el in c2.fetchall()]
            conn.close()

            context = {'opis_pola': opis_pola, 'dodane_skldniki': dodane_skldniki, 'ciasto': ciasto}
            return render_template('skladniki_juz_dodane.html', **context)

        flash('Uzupełnij wszystkie pola!')
        return redirect('/dodanie_skladnika_c')


@dodaj_bp.route('/dodanie_skladnika_k', methods=['GET', 'POST'], endpoint='dodaj_skladniki_k')
@login_required
def dodaj_skladniki_k():
    if request.method == 'GET':
        messages = get_flashed_messages()
        opis_pola = 'Dodaj składnik do kremu/polewy:'
        opis_pola_2 = 'Wybierz krem/polewę: '
        lista_kremow = wszystkie_kremy()
        lista_skladnikow = wszystkie_skladniki()
        context = {'opis_pola': opis_pola, 'opis_pola_2': opis_pola_2, 'lista': lista_kremow,
                   'lista_skladnikow': lista_skladnikow, 'messages': messages}
        return render_template('dodaj_skladniki.html', **context)

    if request.method == 'POST':
        id_k = request.form['id']
        id_skl_k = request.form['id_skl']
        ilosc_skl_k = request.form['ilosc_skl']

        if id_skl_k and ilosc_skl_k:
            conn = sqlite3.connect('baza.db')
            c = conn.cursor()
            c2 = conn.cursor()

            zapytanie = """
            INSERT INTO "kremy_do_skladniki" ("id_k", "id_skl_k", "ilosc_skl_k") VALUES (?, ?, ?)
            """
            parametry = (id_k, id_skl_k, ilosc_skl_k)

            c.execute(zapytanie, (parametry))

            conn.commit()
            opis_pola = 'Do polewy/kremu są dodane następujące składniki: '

            zapytanie_2 = """
                    SELECT s.skladnik FROM "kremy" AS k
                    LEFT JOIN "kremy_do_skladniki" AS kds 
                    ON k.id=kds.id_k
                    LEFT JOIN "skladniki" AS s
                    ON kds.id_skl_k=s.id
                    WHERE k.id = ?
                    """

            c2.execute(zapytanie_2, (id_k,))
            dodane_skldniki = [list(el) for el in c2.fetchall()]

            conn.close()

            context = {'opis_pola': opis_pola, 'dodane_skldniki': dodane_skldniki}
            return render_template('skladniki_juz_dodane.html', **context)

        flash('Uzupełnij wszystkie pola!')
        return redirect('/dodanie_skladnika_k')


@dodaj_bp.route('/dodanie_skladnika_s', methods=['GET', 'POST'], endpoint='dodaj_skladniki_s')
@login_required
def dodaj_skladnik():
    if request.method == 'GET':
        messages = get_flashed_messages()
        opis_pola = 'Nowy_skladnik'
        opis_pola_2 = 'Dodaj nowy składnik:'
        context = {'opis_pola': opis_pola, 'opis_pola_2': opis_pola_2, 'messages': messages}
        return render_template('dodaj_nowy_skladnik.html', **context)

    if request.method == 'POST':
        skladnik = request.form['skladnik']
        conn = get_connection()
        c = conn.cursor()
        zapytanie = """
        SELECT skladnik FROM skladniki
        """
        if skladnik:
            c.execute(zapytanie)
            opis_pola = 'Nowy_skladnik'
            opis_pola_2 = 'Dodaj nowy składnik:'
            opis_pola_3 = 'Nie można dodać tego samego składnika drugi raz.'

            for linia in c:
                for x in linia:
                    if x == skladnik:
                        print(x)
                        context = {'opis_pola': opis_pola, 'opis_pola_2': opis_pola_2, 'opis_pola_3': opis_pola_3}
                        return render_template('dodaj_nowy_skladnik.html', **context)
            else:
                zapytanie = """
                INSERT INTO 'skladniki' VALUES (NULL, ?)
                """
                c.execute(zapytanie, (skladnik,))
                conn.commit()
                conn.close()
                return redirect('/dodanie_skladnika_s')

        flash('Pole "Dodaj nowy składnik" nie może być puste!')
        return redirect('/dodanie_skladnika_s')
