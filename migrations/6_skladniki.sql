DROP TABLE IF EXISTS "skladniki";

CREATE TABLE "skladniki"
(
    "id"        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "skladnik" TEXT NOT NULL
);

INSERT INTO "skladniki"
VALUES (NULL, 'm¹ka przenna'),
       (NULL, 'cukier'),
       (NULL, 'mas³o'),
       (NULL, '¿ó³tka'),
       (NULL, 'sól'),
       (NULL, 'wrz¹ca woda'),
       (NULL, 'cukier puder'),
       (NULL, 'kakao'),
       (NULL, 'twaróg mielony'),
       (NULL, 'jajko'),
       (NULL, 'cukier waniliowy'),
       (NULL, 'm¹ka ziemniaczana'),
       (NULL, 'mak mielony'),
       (NULL, 'tarta bu³ka'),
       (NULL, 'proszek do pieczenia'),
       (NULL, 'aromat migda³owy'),
       (NULL, 'kawa rozpuszczalna'),
       (NULL, 'd¿em pomarañczowy'),
       (NULL, 'serek mascarpone'),
       (NULL, 'œmietana kremówka'),
       (NULL, 'p³atki migda³owe'),
       (NULL, 'bia³ka jaj');