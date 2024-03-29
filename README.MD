**Opis aplikacji:**
- aplikacja ze s�odkimi przepisami kulinarnymi
- w aplikacji mo�na przegl�da� przepisy, wyszukiwa�, a po zalogowaniu doda� lub usun�� przepis
- wymagania - python 3.7+ z zainstalowanym modu�em flask
- dane s� przechowywane w bazie SQLite3
- do tworzenia stron internetowych wykorzystany jest HTML z szablonami Jinja 


**Uruchomienie programu:**
- wszystkie szablony html musz� by� zapisane w katalogu templates znajduj�cym si� w katalogu z pozosta�ymi plikami
- wszystkie pliki tworz�ce tabele sql musz� by� zapisane w katalogu migrations znajduj�cym si� w katalogu z pozosta�ymi plikami
- wszystkie zdj�cia musz� by� zawsze w katalogu static
- pierwszym krokiem jest stworzenie bazy istniej�cych przepis�w uruchamiaj�c plik baza_init.py
- aplikacj� uruchamiamy uruchamiaj�c plik slodkie_przepisy.py

**U�ytkowanie programu:**
- Dodawa� i usuwa� przepisy mog� tylko zalogowani administratorzy, aktualnie sworzone s� 3 profile, pozostali u�ytkownicy maj� mo�liwo�� przegl�dania i wyszukiwania przepis�w.
- Program sk�ada si� z nawigacji zawieraj�cej:
 
    1. Stron� g��wn�:

        - Przywitanie u�ytkownika

    2. Przepisy:
        - List� wszystkich dost�pnych przepis�w z bazy danych.
        - List� przepis�w, kt�ra zawiera tylko ciasta.
        - List� przepis�w, kt�ra zawiera tylko ciasteczka.
        - List� przepis�w, kt�ra zawiera tylko kremy.
        - List� przepis�w, kt�ra zawiera tylko polewy.
        
    3. Znajd� przepis:
        - U�ytkowik mo�e wyszyka� przepis wpisuj�c nazw� przepisu lub cz�� nazwy przepisu(wyszukuje tylko ca�e przepisy, nie mo�na wyszuka� samego kremu lub polewy).

    4. Logowanie:
        - Logowanie.
        - Wylogowanie.
    
    **Opcje dost�pne dopiero po zalogowaniu administratora:**
     
    5. Dodaj:        
        - Jak doda� przepis - opis w jaki sposub doda� nowy pe�en przepis do bazy.
        - Dodanie nowego sk�adnika - dodajemy sk�adnik do bazy sk�adniki.
        - Dodanie kremu - dodajemy nazw� kremu/polewy oraz spos�b jego przygotowania do bazy kremy, je�li przepis sk�ada si� r�wnie� z kremu lub polewy to trzeba najpier uzupe�ni� t� zak�adk� zanim dodanym ca�y przepis, dalej zostajemy przekierowani na stron� dodania sk�adnik�w do ciasta/ciasteczek.
        - Dodanie ciasta - dodajemy nazw� ciasta oraz spos�b jego przygotowania do bazy ciasta, je�li ciasto/ciasteczka sk�adna si� r�wnie� z kremu lub polewy to koniecznie trzeba wybra� j� z rozwijanej listy, tu te� mo�emy poda� nr zdj�cia jakie ma by� do��czone do przepisu (pole nie jest obowi�zkowe), dalej zostajemy przekierowani na stron� dodania sk�adnik�w do kremu/polewy.
        - Dodaj�c zdj�cie trzeba je najpierw umie�ci� w katalogu static, a potem poda� nazw� przy dodawaniu ciasta.
        - Dodanie sk�adnika do kremu - do ka�dego ciasta/ciasteczek mo�emy doda� kolejne sk�adniki w dowolnym mom�cie.
        - Dodanie sk�adnika do ciasta - do ka�dego kremu/polewy mo�emy doda� kolejne sk�adniki w dowolnym mom�cie.
        
    6. Usu�:
        - Usuni�cie ciasta/ciasteczek - usuwa wybrane ciasto/ciasteczka jak r�wnie� przypisany krem/polew� je�li nie jest powi�zany z innym przepisem oraz sk�adniki je�li nie s� powi�zane z innym przepisem.
        