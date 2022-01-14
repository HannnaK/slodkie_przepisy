DROP TABLE IF EXISTS "users";
CREATE TABLE "users"
(
    "id"       INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    "username" TEXT    NOT NULL,
    "password" TEXT    NOT NULL
);

INSERT INTO "users"
VALUES (1, 'pat', 'pbkdf2:sha256:150000$Mu7RycuK$014db8624b9620065015ae1051ac8145c1a8c91d908af0097001ebc0ee9f2894'),
       (2, 'mat', 'pbkdf2:sha256:150000$kpWdSuYB$50dbcb245e379c05f28d6318ca95ad5e37d8f146a5900f847bf47dc3131e40aa'),
       (3, 'ola', 'pbkdf2:sha256:150000$mzQsfPNm$bc966f183e329abef20e0603b3d49fa40b955ed4ffc3b5a20470f086171b63f4');