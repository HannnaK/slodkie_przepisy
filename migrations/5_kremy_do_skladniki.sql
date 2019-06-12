DROP TABLE IF EXISTS "kremy_do_skladniki";

CREATE TABLE "kremy_do_skladniki"
(
    "id"        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "id_k"     INTEGER NOT NULL,
    "id_skl_k"    INTEGER NOT NULL,
    "ilosc_skl_k" TEXT NOT NULL
);

INSERT INTO "kremy_do_skladniki"
VALUES (NULL, 1, 6, '3 造磬i'),
       (NULL, 1, 7, '3 造磬i'),
       (NULL, 1, 3, '100g'),
       (NULL, 1, 8, '3 造磬i'),

       (NULL, 2, 17, '8 造瞠czek'),
       (NULL, 2, 6, '2 造磬i'),
       (NULL, 2, 19, '750g'),
       (NULL, 2, 20, '375g'),
       (NULL, 2, 7, '80g');


