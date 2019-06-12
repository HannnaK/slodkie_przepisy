import sqlite3


def get_connection():
    conn = sqlite3.connect('baza.db')
    conn.row_factory = sqlite3.Row
    return conn


def wszystkie_przepisy():
    conn = get_connection()
    c = conn.cursor()
    zapytanie = """
    SELECT "id", "nazwa"  FROM "ciasta" ORDER BY "nazwa" ASC;
    """
    c.execute(zapytanie)
    lista_przepisow = []
    for linia in c:
        lista_przepisow.append(linia)

    return lista_przepisow


def wszystkie_kremy():
    conn = get_connection()
    c = conn.cursor()
    zapytanie = """
    SELECT "id", "nazwa" FROM "kremy" ORDER BY "nazwa" ASC
    """
    c.execute(zapytanie)
    lista_kremow = []
    for linia in c:
        lista_kremow.append(linia)

    return lista_kremow


def wszystkie_skladniki():
    conn = get_connection()
    c = conn.cursor()
    zapytanie = """
    SELECT "id", "skladnik" FROM skladniki ORDER BY "skladnik" ASC
    """
    c.execute(zapytanie)
    lista_skladnikow = []
    for linia in c:
        lista_skladnikow.append(linia)

    return lista_skladnikow


def wyselekcjonowane_przepisy(zapytanie, rodzaj):
    conn = get_connection()
    c = conn.cursor()
    c.execute(zapytanie, (rodzaj,))
    lista = []
    for linia in c:
        lista.append(linia)
    conn.close()

    return lista


def pozostale_skl(cursor):
    skladniki_cds_kds = []
    for linia in cursor:
        for x in linia:
            skladniki_cds_kds.append(x)
    return skladniki_cds_kds


def wszystkie_zdjecia():
    conn = get_connection()
    c = conn.cursor()
    zapytanie = """SELECT "nr_zdjecia" FROM "ciasta" """
    c.execute(zapytanie)
    zdjecia = []
    for linia in c:
        zdjecia.append(linia)
    conn.close()
    return zdjecia

def krem_bez_skl(fraza):
    conn = sqlite3.connect('baza.db')
    c = conn.cursor()
    zapytanie = """
        SELECT k.id, k.nazwa, c.id, c.id_k, k.przygotowanie FROM ciasta AS c
        JOIN kremy AS k
        ON c.id_k==k.id
        WHERE c.id=?
        """
    c.execute(zapytanie, (fraza,))

    krem_bez_skladnikow = []
    for linia in c:
        krem_bez_skladnikow.append((linia))

    return krem_bez_skladnikow


