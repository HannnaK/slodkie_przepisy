DROP TABLE IF EXISTS "kremy";

CREATE TABLE "kremy"
(
    "id"        INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "nazwa"     TEXT NOT NULL,
    "rodzaj"    TEXT NOT NULL,
    "przygotowanie" TEXT NOT NULL
);

INSERT INTO "kremy"
VALUES (NULL,'Polewa czekoladowa', 'polewa',
        'Do rondelka wlaæ wodê i rozpuœciæ w niej cukier (kolejnoœæ rozpuszczania poszczególnych sk³adników jest wa¿na, poszczególne sk³adniki siê nam nie zwa¿¹ i nie "rozwarstwi¹"). Nastêpnie dodajemy pokrojone na ma³e kawa³eczki mas³o i rozpuszczamy. Zdejmujemy z ognia i wsypujemy przesiane kakao. Energicznie mieszamy by powsta³a g³adka, lœni¹ca polewa, polewamy ciasto. Do mojego mazurka potrzebne 3 porcje'),
        (NULL, 'Krem kawowy', 'krem', 'Kawê rozpuœciæ w wodzie i zimn¹ wymieszaæ z serkiem mascarpone. Œmietanê kremówkê ubiæ na sztywno, pod koniec ubijania dodawaæ stopniowo cukier puder i dalej ubijaæ. Dodaæ serek mascarpone i zmiksowaæ na ma³ych obrotach do po³¹czenia siê sk³adników.');