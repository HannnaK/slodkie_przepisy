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
        'Do rondelka wla� wod� i rozpu�ci� w niej cukier (kolejno�� rozpuszczania poszczeg�lnych sk�adnik�w jest wa�na, poszczeg�lne sk�adniki si� nam nie zwa�� i nie "rozwarstwi�"). Nast�pnie dodajemy pokrojone na ma�e kawa�eczki mas�o i rozpuszczamy. Zdejmujemy z ognia i wsypujemy przesiane kakao. Energicznie mieszamy by powsta�a g�adka, l�ni�ca polewa, polewamy ciasto. Do mojego mazurka potrzebne 3 porcje'),
        (NULL, 'Krem kawowy', 'krem', 'Kaw� rozpu�ci� w wodzie i zimn� wymiesza� z serkiem mascarpone. �mietan� krem�wk� ubi� na sztywno, pod koniec ubijania dodawa� stopniowo cukier puder i dalej ubija�. Doda� serek mascarpone i zmiksowa� na ma�ych obrotach do po��czenia si� sk�adnik�w.');