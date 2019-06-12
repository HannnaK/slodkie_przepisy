import sqlite3

conn = sqlite3.connect('baza.db')
c = conn.cursor()


def wykonaj_skrypt_sql(skrypt):
    with open(skrypt) as f:
        zapytanie = f.read()
    c.executescript(zapytanie)


wykonaj_skrypt_sql('migrations\\1_drop_tables.sql')
wykonaj_skrypt_sql('migrations\\2_ciasta.sql')
wykonaj_skrypt_sql('migrations\\3_kremy.sql')
wykonaj_skrypt_sql('migrations\\4_ciasta_do_skladniki.sql')
wykonaj_skrypt_sql('migrations\\5_kremy_do_skladniki.sql')
wykonaj_skrypt_sql('migrations\\6_skladniki.sql')
wykonaj_skrypt_sql('migrations\\7_users.sql')

conn.commit()

conn.close()
