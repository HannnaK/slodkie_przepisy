DROP TABLE IF EXISTS "skladniki";

CREATE TABLE "skladniki"
(
    "id"        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "skladnik" TEXT NOT NULL
);

INSERT INTO "skladniki"
VALUES (NULL, 'mąka przenna'),
       (NULL, 'cukier'),
       (NULL, 'masło'),
       (NULL, 'żółtka'),
       (NULL, 'sól'),
       (NULL, 'wrząca woda'),
       (NULL, 'cukier puder'),
       (NULL, 'kakao'),
       (NULL, 'twaróg mielony'),
       (NULL, 'jajko'),
       (NULL, 'cukier waniliowy'),
       (NULL, 'mąka ziemniaczana'),
       (NULL, 'mak mielony'),
       (NULL, 'tarta bułka'),
       (NULL, 'proszek do pieczenia'),
       (NULL, 'aromat migdałowy'),
       (NULL, 'kawa rozpuszczalna'),
       (NULL, 'dżem pomarańczowy'),
       (NULL, 'serek mascarpone'),
       (NULL, 'śmietana kremówka'),
       (NULL, 'płatki migdałowe'),
       (NULL, 'białka jaj');