DROP TABLE IF EXISTS "skladniki";

CREATE TABLE "skladniki"
(
    "id"        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "skladnik" TEXT NOT NULL
);

INSERT INTO "skladniki"
VALUES (NULL, 'm�ka przenna'),
       (NULL, 'cukier'),
       (NULL, 'mas�o'),
       (NULL, '��tka'),
       (NULL, 's�l'),
       (NULL, 'wrz�ca woda'),
       (NULL, 'cukier puder'),
       (NULL, 'kakao'),
       (NULL, 'twar�g mielony'),
       (NULL, 'jajko'),
       (NULL, 'cukier waniliowy'),
       (NULL, 'm�ka ziemniaczana'),
       (NULL, 'mak mielony'),
       (NULL, 'tarta bu�ka'),
       (NULL, 'proszek do pieczenia'),
       (NULL, 'aromat migda�owy'),
       (NULL, 'kawa rozpuszczalna'),
       (NULL, 'd�em pomara�czowy'),
       (NULL, 'serek mascarpone'),
       (NULL, '�mietana krem�wka'),
       (NULL, 'p�atki migda�owe'),
       (NULL, 'bia�ka jaj');