from flask import Blueprint, request, render_template, redirect, flash
from slodkie_przepisy_funkcje import wszystkie_przepisy, pozostale_skl
from slodkie_przepisy_logowanie import login_required
import sqlite3

usun_bp = Blueprint('usun_endpoints', __name__)


@usun_bp.route('/usun_ciasto', methods=['GET', 'POST'], endpoint='usun_ciasto')
@login_required
def usun_ciasto():
    if request.method == 'GET':
        opis_pola = 'Usun_ciasto'
        opis_pola_2 = 'Wybierz ciasto/ciasteczka do usunięcia'
        lista_przepisow = wszystkie_przepisy()
        context = {'opis_pola': opis_pola, 'opis_pola_2': opis_pola_2, 'lista': lista_przepisow}
        return render_template('usun.html', **context)

    if request.method == 'POST':
        id = request.form['id']

        conn = sqlite3.connect('baza.db')

        c = conn.cursor()
        c1 = conn.cursor()

        zapytanie1 = """
        SELECT c.id, c.id_k, s.id FROM "ciasta" AS c
        LEFT JOIN "ciasta_do_skladniki" AS cds 
        ON c.id=cds.id_c
        LEFT JOIN "skladniki" AS s
        ON cds.id_skl_c=s.id
        LEFT JOIN "kremy" AS k
        ON c.id_k=k.id
        WHERE c.id = ?
        """
        c.execute(zapytanie1, (id,))
        ids_kasowanego_przepisu = []  # krotki (id_c, id_k, id_s) kasowanego przepisu
        for linia in c:
            ids_kasowanego_przepisu.append(linia)

        zapytanie2 = """   
        SELECT s.id FROM skladniki AS s
        JOIN kremy AS k
        ON kds.id_skl_k=s.id
        JOIN "kremy_do_skladniki" AS kds
        ON k.id=kds.id_k
        WHERE k.id=?
        """
        c.execute(zapytanie2, (ids_kasowanego_przepisu[0][1],))
        skladniki_do_usuniecia_k = []  # lista id składników usuwanego kremu
        for linia in c:
            skladniki_do_usuniecia_k.append(linia[0])

        zapytanie3 = """
        SELECT c.id, c.id_k, s.id FROM "ciasta" AS c
        LEFT JOIN "ciasta_do_skladniki" AS cds 
        ON c.id=cds.id_c
        LEFT JOIN "skladniki" AS s
        ON cds.id_skl_c=s.id
        LEFT JOIN "kremy" AS k
        ON c.id_k=k.id
        """
        c.execute(zapytanie3)
        ids_wszystkich_przepisow = []  # krotki (id_c, id_k, id_s) do wszystkich przepisów
        for linia in c:
            ids_wszystkich_przepisow.append(linia)

        przepisy_powiazane_z_kremem = []
        for ids in ids_wszystkich_przepisow:
            if ids[1] == ids_kasowanego_przepisu[0][1] and ids[1] != '':
                przepisy_powiazane_z_kremem.append(ids[0])

        przepisy_powiazane_z_kremem = set(przepisy_powiazane_z_kremem)

        if len(
                przepisy_powiazane_z_kremem) == 1:  # jeśli krem/polewa nie jest powiązany z innym przepisem zostanie usunięty z tabeli kremy
            zapytanie4 = """
            DELETE FROM "kremy" WHERE id = ?
            """
            c.execute(zapytanie4, (ids_kasowanego_przepisu[0][1],))
            conn.commit()

        skladnik_do_usuniecia_c = []
        for ids in ids_kasowanego_przepisu:
            skladnik_do_usuniecia_c.append(ids[2])

        skladnik_do_usuniecia = skladnik_do_usuniecia_c + skladniki_do_usuniecia_k

        skladnik_do_usuniecia = set(skladnik_do_usuniecia)
        skladnik_do_usuniecia = list(skladnik_do_usuniecia)

        zapytanie5 = """
        DELETE FROM "ciasta" WHERE id = ?
        """
        c.execute(zapytanie5, (id,))
        conn.commit()

        zapytanie6 = """
        DELETE FROM ciasta_do_skladniki WHERE id_c=?
        """
        c.execute(zapytanie6, (id,))
        conn.commit()

        if len(
                przepisy_powiazane_z_kremem) == 1:  # jeśli krem/polewa nie jest powiązany z innym przepisem zostanie usunięty z tabeli kremy_do_skladniki
            zapytanie7 = """
            DELETE FROM kremy_do_skladniki WHERE id_k=?
            """
            c.execute(zapytanie7, (ids_kasowanego_przepisu[0][1],))
            conn.commit()

        zapytanie8 = """
        SELECT id_skl_c FROM ciasta_do_skladniki      
        """
        c.execute(zapytanie8)

        zapytanie9 = """
        SELECT id_skl_k FROM kremy_do_skladniki      
        """
        c1.execute(zapytanie9)

        pozostale_skladniki = pozostale_skl(c) + pozostale_skl(c1)
        # skladniki przypisane do pozostałych przepisów

        pozostale_skladniki = set(pozostale_skladniki)
        pozostale_skladniki = list(pozostale_skladniki)

        for skl in skladnik_do_usuniecia:  # usunięcie składnika który nie jest powiazany z innymi przepisami
            if skl not in pozostale_skladniki:
                zapytanie10 = """
                DELETE FROM skladniki WHERE id=?
                """
                c.execute(zapytanie10, (skl,))
                conn.commit()

        conn.close()

        flash('Przepis został usunięty!')
        return redirect('/')
