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
        'Z podanych sk³adników zagnieœæ ciasto i w³o¿yæ je na godzinê do lodówki. Nastêonie wyj¹æ i roz³o¿yæ na blasze w formie placaka ( gruboœci oko³o 1 cm). Piec oko³o 15 minut na z³oty kolor w temp. 200C.', 1, 1),
       (NULL, 'Sernik', 'ciasto',
        '¯ó³tka oddzielamy od bia³ek. Z bia³ek ubijamy sztywn¹ pianê. Mas³o ucieramy z cukrem pudrem i cukrem waniliowym. Dodajemy po jednym ¿ó³tku ca³y czas ucieraj¹c. Nastêpnie masê maœlano-jajeczn¹ miksujemy z twarogiem. Wsypujemy obydwa rodzaje m¹ki. Na koniec dodajemy pianê z bia³ek i delikatnie mieszamy. Ca³oœæ przek³adamy do wysmarowanej mas³em i oprószonej bu³k¹ tart¹ formy. Pieczemy ca 60 minut w temp. 170C. Po tym czasie wy³¹czamy piekarnik i pozostawiamy w nim sernik do ca³kowitego ostygniêcia (przy zamkniêtych drzwiczkach).', NULL, 2),
        (NULL, 'Tort Kawowy', 'ciasto', 'Mak, bu³kê tart¹ i proszek do pieczenia wymieszaæ. Wlaæ wrz¹c¹ wodê i ponownie wymieszaæ. ¯ó³tka utrzeæ z cukrem na puszyst¹ masê, dodaæ do maku i wymieszaæ, dodaæ aromat i ponownie wymieszaæ. Bia³ka ubiæ na sztywn¹ pianê, dodaæ do maku i delikatnie wymieszaæ. Tortownicê o œrednicy 28 cm wy³o¿yæ papierem do pieczenia, prze³o¿yæ ciasto i piec 1,5 h w temperaturze 175 stopni C. Wyj¹æ z piekarnika i wystudziæ w foremce. Ciasto makowe przekroiæ na 3 blaty. Na paterze u³o¿yæ pierwszy blat, nas¹czyæ delikatnie sokiem z pomarañczy, posmarowaæ cienko d¿emem z pomarañczy i wy³o¿yæ 1/4 czêœæ kremu mascarpone. Przykryæ drugim blatem, nas¹czyæ sokiem, posmarowaæ reszt¹ d¿emeu i znów 1/4 czêœæ kremu mascarpone. Przykryæ trzecim blatem, nas¹czyæ sokiem, wy³o¿yæ 1/4 czêœæ kremu mascarpone i wyrównaæ. Pozosta³y krem rozsmarowaæ na boki, zostawiaj¹c trochê na dekoracjê.', 2, 3),
        (NULL, 'Ciasteczka migda³owe', 'ciasteczka', 'Do miski w³o¿yæ p³atki migda³owe, cukier, m¹kê i wymieszaæ z bia³kami. Nastêpnie wlaæ rozpuszczone letnie mas³o i wymieszaæ. Odstawiæ na 30 min. Uk³adaæ niewielkie kulki na matê do pieczenia i widelcem zmoczonym w wodzie rozklepaæ p³askie kó³ka. Piec w temp. 180 C ok. 20 min.', NULL, 4);