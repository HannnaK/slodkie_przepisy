**Opis aplikacji:**
- aplikacja ze s³odkimi przepisami kulinarnymi
- w aplikacji mo¿na przegl¹daæ przepisy, wyszukiwaæ, a po zalogowaniu dodaæ lub usun¹æ przepis
- wymagania - python 3.7+ z zainstalowanym modu³em flask
- dane s¹ przechowywane w bazie SQLite3
- do tworzenia stron internetowych wykorzystany jest HTML z szablonami Jinja 


**Uruchomienie programu:**
- wszystkie szablony html musz¹ byæ zapisane w katalogu templates znajduj¹cym siê w katalogu z pozosta³ymi plikami
- wszystkie pliki tworz¹ce tabele sql musz¹ byæ zapisane w katalogu migrations znajduj¹cym siê w katalogu z pozosta³ymi plikami
- wszystkie zdjêcia musz¹ byæ zawsze w katalogu static
- pierwszym krokiem jest stworzenie bazy istniej¹cych przepisów uruchamiaj¹c plik baza_init.py
- aplikacjê uruchamiamy uruchamiaj¹c plik slodkie_przepisy.py

**U¿ytkowanie programu:**
- Dodawaæ i usuwaæ przepisy mog¹ tylko zalogowani administratorzy, aktualnie sworzone s¹ 3 profile, pozostali u¿ytkownicy maj¹ mo¿liwoœæ przegl¹dania i wyszukiwania przepisów.
- Program sk³ada siê z nawigacji zawieraj¹cej:
 
    1. Stronê g³ówn¹:

        - Przywitanie u¿ytkownika

    2. Przepisy:
        - Listê wszystkich dostêpnych przepisów z bazy danych.
        - Listê przepisów, która zawiera tylko ciasta.
        - Listê przepisów, która zawiera tylko ciasteczka.
        - Listê przepisów, która zawiera tylko kremy.
        - Listê przepisów, która zawiera tylko polewy.
        
    3. ZnajdŸ przepis:
        - U¿ytkowik mo¿e wyszykaæ przepis wpisuj¹c nazwê przepisu lub czêœæ nazwy przepisu(wyszukuje tylko ca³e przepisy, nie mo¿na wyszukaæ samego kremu lub polewy).

    4. Logowanie:
        - Logowanie.
        - Wylogowanie.
    
    **Opcje dostêpne dopiero po zalogowaniu administratora:**
     
    5. Dodaj:        
        - Jak dodaæ przepis - opis w jaki sposub dodaæ nowy pe³en przepis do bazy.
        - Dodanie nowego sk³adnika - dodajemy sk³adnik do bazy sk³adniki.
        - Dodanie kremu - dodajemy nazwê kremu/polewy oraz sposób jego przygotowania do bazy kremy, jeœli przepis sk³ada siê równie¿ z kremu lub polewy to trzeba najpier uzupe³niæ t¹ zak³adkê zanim dodanym ca³y przepis, dalej zostajemy przekierowani na stronê dodania sk³adników do ciasta/ciasteczek.
        - Dodanie ciasta - dodajemy nazwê ciasta oraz sposób jego przygotowania do bazy ciasta, jeœli ciasto/ciasteczka sk³adna siê równie¿ z kremu lub polewy to koniecznie trzeba wybraæ j¹ z rozwijanej listy, tu te¿ mo¿emy podaæ nr zdjêcia jakie ma byæ do³¹czone do przepisu (pole nie jest obowi¹zkowe), dalej zostajemy przekierowani na stronê dodania sk³adników do kremu/polewy.
        - Dodaj¹c zdjêcie trzeba je najpierw umieœciæ w katalogu static, a potem podaæ nazwê przy dodawaniu ciasta.
        - Dodanie sk³adnika do kremu - do ka¿dego ciasta/ciasteczek mo¿emy dodaæ kolejne sk³adniki w dowolnym momêcie.
        - Dodanie sk³adnika do ciasta - do ka¿dego kremu/polewy mo¿emy dodaæ kolejne sk³adniki w dowolnym momêcie.
        
    6. Usuñ:
        - Usuniêcie ciasta/ciasteczek - usuwa wybrane ciasto/ciasteczka jak równie¿ przypisany krem/polewê jeœli nie jest powi¹zany z innym przepisem oraz sk³adniki jeœli nie s¹ powi¹zane z innym przepisem.
        