DROP TABLE IF EXISTS "ciasta";

CREATE TABLE "ciasta"
(
    "id"        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "nazwa"     TEXT NOT NULL,
    "rodzaj"    TEXT NOT NULL,
    "przygotowanie" TEXT NOT NULL,
    "id_k"      TEXT,
    "nr_zdjecia" TEXT
);

INSERT INTO "ciasta"
VALUES (NULL, 'Mazurek', 'ciasto',
        'Z podanych sk�adnik�w zagnie�� ciasto i w�o�y� je na godzin� do lod�wki. Nast�onie wyj�� i roz�o�y� na blasze w formie placaka ( grubo�ci oko�o 1 cm). Piec oko�o 15 minut na z�oty kolor w temp. 200C.', 1, 1),
       (NULL, 'Sernik', 'ciasto',
        '��tka oddzielamy od bia�ek. Z bia�ek ubijamy sztywn� pian�. Mas�o ucieramy z cukrem pudrem i cukrem waniliowym. Dodajemy po jednym ��tku ca�y czas ucieraj�c. Nast�pnie mas� ma�lano-jajeczn� miksujemy z twarogiem. Wsypujemy obydwa rodzaje m�ki. Na koniec dodajemy pian� z bia�ek i delikatnie mieszamy. Ca�o�� przek�adamy do wysmarowanej mas�em i opr�szonej bu�k� tart� formy. Pieczemy ca 60 minut w temp. 170C. Po tym czasie wy��czamy piekarnik i pozostawiamy w nim sernik do ca�kowitego ostygni�cia (przy zamkni�tych drzwiczkach).', NULL, 2),
        (NULL, 'Tort Kawowy', 'ciasto', 'Mak, bu�k� tart� i proszek do pieczenia wymiesza�. Wla� wrz�c� wod� i ponownie wymiesza�. ��tka utrze� z cukrem na puszyst� mas�, doda� do maku i wymiesza�, doda� aromat i ponownie wymiesza�. Bia�ka ubi� na sztywn� pian�, doda� do maku i delikatnie wymiesza�. Tortownic� o �rednicy 28 cm wy�o�y� papierem do pieczenia, prze�o�y� ciasto i piec 1,5 h w temperaturze 175 stopni C. Wyj�� z piekarnika i wystudzi� w foremce. Ciasto makowe przekroi� na 3 blaty. Na paterze u�o�y� pierwszy blat, nas�czy� delikatnie sokiem z pomara�czy, posmarowa� cienko d�emem z pomara�czy i wy�o�y� 1/4 cz�� kremu mascarpone. Przykry� drugim blatem, nas�czy� sokiem, posmarowa� reszt� d�emeu i zn�w 1/4 cz�� kremu mascarpone. Przykry� trzecim blatem, nas�czy� sokiem, wy�o�y� 1/4 cz�� kremu mascarpone i wyr�wna�. Pozosta�y krem rozsmarowa� na boki, zostawiaj�c troch� na dekoracj�.', 2, 3),
        (NULL, 'Ciasteczka migda�owe', 'ciasteczka', 'Do miski w�o�y� p�atki migda�owe, cukier, m�k� i wymiesza� z bia�kami. Nast�pnie wla� rozpuszczone letnie mas�o i wymiesza�. Odstawi� na 30 min. Uk�ada� niewielkie kulki na mat� do pieczenia i widelcem zmoczonym w wodzie rozklepa� p�askie k�ka. Piec w temp. 180 C ok. 20 min.', NULL, 4);