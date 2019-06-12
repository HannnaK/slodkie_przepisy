DROP TABLE IF EXISTS "ciasta_do_skladniki";

CREATE TABLE "ciasta_do_skladniki"
(
    "id"        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "id_c"     INTEGER NOT NULL,
    "id_skl_c"    INTEGER NOT NULL,
    "ilosc_skl_c" TEXT NOT NULL
);

INSERT INTO "ciasta_do_skladniki"
VALUES (NULL, 1, 1, '1kg'),
       (NULL, 1, 2, '350g'),
       (NULL, 1, 3, '600g'),
       (NULL, 1, 4, '5szt.'),
       (NULL, 1, 5, 'szczypta'),

       (NULL, 2, 9, '1kg'),
       (NULL, 2, 10, '8szt.'),
       (NULL, 2, 3, '125g'),
       (NULL, 2, 7, '60g'),
       (NULL, 2, 11, '1 opakowanie'),
       (NULL, 2, 1, 'czubata 造磬a'),
       (NULL, 2, 12, 'czubata 造磬a'),

       (NULL, 3, 13, '210g'),
       (NULL, 3, 2, '1,5 szkl.'),
       (NULL, 3, 14, '90g'),
       (NULL, 3, 6, '15 造瞠k'),
       (NULL, 3, 10, '13 szt.'),
       (NULL, 3, 15, '2,5 造瞠czki'),
       (NULL, 3, 18, '250g'),
       (NULL, 3, 16, '1 造瞠czka'),

       (NULL, 4, 21, '100g'),
       (NULL, 4, 2, '60g'),
       (NULL, 4, 1, '15g'),
       (NULL, 4, 22, '2 szt.'),
       (NULL, 4, 3, '20g');

