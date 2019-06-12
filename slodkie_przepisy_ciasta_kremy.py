from flask import Blueprint, render_template
from slodkie_przepisy_funkcje import wszystkie_przepisy, wyselekcjonowane_przepisy, wszystkie_zdjecia, krem_bez_skl
import sqlite3

przepis_bp = Blueprint('przepis_endpoints', __name__)


@przepis_bp.route('/przepisy')
def przepisy():
    lista_ciast = wszystkie_przepisy()

    return render_template('lista_przepisow.html', lista_ciast=lista_ciast)


ciasto_ciasteczka = """
SELECT "id", "nazwa"  FROM "ciasta" WHERE "rodzaj"=? ORDER BY "nazwa" ASC;
"""

kremy_polewy = """
SELECT "id", "nazwa"  FROM "kremy" WHERE "rodzaj"=? ORDER BY "nazwa" ASC;
"""


@przepis_bp.route('/ciasta')
def ciasta():
    lista_ciast = wyselekcjonowane_przepisy(ciasto_ciasteczka, 'ciasto')
    return render_template('lista_przepisow.html', lista_ciast=lista_ciast)


@przepis_bp.route('/ciasteczka')
def ciasteczka():
    lista_ciast = wyselekcjonowane_przepisy(ciasto_ciasteczka, 'ciasteczka')
    return render_template('lista_przepisow.html', lista_ciast=lista_ciast)


@przepis_bp.route('/kremy')
def kremy():
    lista_dodatkow = wyselekcjonowane_przepisy(kremy_polewy, 'krem')
    return render_template('lista_przepisow.html', lista_dodatkow=lista_dodatkow)


@przepis_bp.route('/polewy')
def polewy():
    lista_dodatkow = wyselekcjonowane_przepisy(kremy_polewy, 'polewa')
    return render_template('lista_przepisow.html', lista_dodatkow=lista_dodatkow)


@przepis_bp.route('/ciasto/<int:indeks>')
def przepis(indeks):
    conn = sqlite3.connect('baza.db')
    c1 = conn.cursor()
    c2 = conn.cursor()

    zapytanie_1 = """
    SELECT c.id, c.nazwa, c.rodzaj, c.przygotowanie, c.id_k, s.*, cds.ilosc_skl_c, k.id, c.nr_zdjecia FROM "ciasta" AS c
    LEFT JOIN "ciasta_do_skladniki" AS cds 
    ON c.id=cds.id_c
    LEFT JOIN "skladniki" AS s
    ON cds.id_skl_c=s.id
    LEFT JOIN "kremy" AS k
    ON c.id_k=k.id
    WHERE c.id = ?
    """
    fraza = int(indeks)
    c1.execute(zapytanie_1, (fraza,))

    przepis = []

    for linia in c1:
        przepis.append(linia)

    krem_bez_skladnikow = krem_bez_skl(fraza)

    zapytanie_2 = """
    SELECT k.*, kds.ilosc_skl_k, s.skladnik, c.id, c.id_k FROM kremy AS k, ciasta AS c
    JOIN "skladniki" AS s
    ON kds.id_skl_k=s.id
    JOIN "kremy_do_skladniki" AS kds
    ON k.id=kds.id_k
    WHERE c.id_k=k.id
    """
    c2.execute(zapytanie_2)

    lista_kremow = []

    for linia in c2:
        lista_kremow.append(linia)
    krem = []
    if przepis:
        for k in lista_kremow:
            if k[0] == przepis[0][8]:
                krem.append(k)

    conn.close()
    zdjecia = wszystkie_zdjecia()
    context = {'indeks': indeks, 'przepis': przepis, 'krem': krem, 'zdjecia': zdjecia,
               'krem_bez_skladnikow': krem_bez_skladnikow}
    return render_template('przepis.html', **context)


@przepis_bp.route('/krem/<int:indeks>')
def przepis_krem(indeks):
    conn = sqlite3.connect('baza.db')
    c = conn.cursor()

    zapytanie = """
    SELECT k.*, kds.ilosc_skl_k, s.skladnik FROM kremy AS k
    JOIN "skladniki" AS s
    ON kds.id_skl_k=s.id
    JOIN "kremy_do_skladniki" AS kds
    ON k.id=kds.id_k
    WHERE k.id=?
    """
    fraza = int(indeks)
    c.execute(zapytanie, (fraza,))

    krem = []
    for linia in c:
        krem.append(linia)

    zapytanie = """
    SELECT id, nazwa, przygotowanie from kremy
    WHERE id=?
    """
    c.execute(zapytanie, (fraza,))

    krem_bez_skladnikow = []
    for linia in c:
        krem_bez_skladnikow.append((linia))

    conn.close()

    context = {'indeks': indeks, 'krem': krem, 'krem_bez_skladnikow': krem_bez_skladnikow}
    return render_template('przepis_krem.html', **context)
