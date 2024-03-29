**APPLICATION DESCRIPTION:**
- application with sweet recipes
- in the application, you can view recipes, search, and after logging in, add or delete a recipe
- requirements - python 3.7+ with flask module installed
- to create the database run baza_init.py
- the data are stored in the database SQLite3

**Launching the app:**
- we run the application using the slodkie_przepisy.py file

**Application page:**
- <http://slodkosci.pythonanywhere.com/>
- test user:
    - login: `ola`
    - password: `ola`




********************************************************************************************************************************



**Opis aplikacji:**
- aplikacja ze słodkimi przepisami kulinarnymi
- w aplikacji można przeglądać przepisy, wyszukiwać, a po zalogowaniu dodać lub usunąć przepis
- wymagania - python 3.7+ z zainstalowanym modułem flask
- dane są przechowywane w bazie SQLite3
- do tworzenia stron internetowych wykorzystany jest HTML z szablonami Jinja 


**Uruchomienie programu:**
- wszystkie szablony html muszą być zapisane w katalogu templates znajdującym się w katalogu z pozostałymi plikami
- wszystkie pliki tworzące tabele sql muszą być zapisane w katalogu migrations znajdującym się w katalogu z pozostałymi plikami
- wszystkie zdjęcia muszą być zawsze w katalogu static
- pierwszym krokiem jest stworzenie bazy istniejących przepisów uruchamiając plik baza_init.py
- aplikację uruchamiamy uruchamiając plik slodkie_przepisy.py

**Użytkowanie programu:**
- Dodawać i usuwać przepisy mogą tylko zalogowani administratorzy, aktualnie sworzone są 3 profile, pozostali użytkownicy mają możliwość przeglądania i wyszukiwania przepisów.
- Program składa się z nawigacji zawierającej:
 
    1. Stronę główną:

        - Przywitanie użytkownika

    2. Przepisy:
        - Listę wszystkich dostępnych przepisów z bazy danych.
        - Listę przepisów, która zawiera tylko ciasta.
        - Listę przepisów, która zawiera tylko ciasteczka.
        - Listę przepisów, która zawiera tylko kremy.
        - Listę przepisów, która zawiera tylko polewy.
        
    3. Znajdź przepis:
        - Użytkowik może wyszykać przepis wpisując nazwę przepisu lub część nazwy przepisu(wyszukuje tylko całe przepisy, nie można wyszukać samego kremu lub polewy).

    4. Logowanie:
        - Logowanie.
        - Wylogowanie.
    
    **Opcje dostępne dopiero po zalogowaniu administratora:**
     
    5. Dodaj:        
        - Jak dodać przepis - opis w jaki sposub dodać nowy pełen przepis do bazy.
        - Dodanie nowego składnika - dodajemy składnik do bazy składniki.
        - Dodanie kremu - dodajemy nazwę kremu/polewy oraz sposób jego przygotowania do bazy kremy, jeśli przepis składa się również z kremu lub polewy to trzeba najpier uzupełnić tą zakładkę zanim dodanym cały przepis, dalej zostajemy przekierowani na stronę dodania składników do ciasta/ciasteczek.
        - Dodanie ciasta - dodajemy nazwę ciasta oraz sposób jego przygotowania do bazy ciasta, jeśli ciasto/ciasteczka składna się również z kremu lub polewy to koniecznie trzeba wybrać ją z rozwijanej listy, tu też możemy podać nr zdjęcia jakie ma być dołączone do przepisu (pole nie jest obowiązkowe), dalej zostajemy przekierowani na stronę dodania składników do kremu/polewy.
        - Dodając zdjęcie trzeba je najpierw umieścić w katalogu static, a potem podać nazwę przy dodawaniu ciasta.
        - Dodanie składnika do kremu - do każdego ciasta/ciasteczek możemy dodać kolejne składniki w dowolnym momęcie.
        - Dodanie składnika do ciasta - do każdego kremu/polewy możemy dodać kolejne składniki w dowolnym momęcie.
        
    6. Usuń:
        - Usunięcie ciasta/ciasteczek - usuwa wybrane ciasto/ciasteczka jak również przypisany krem/polewę jeśli nie jest powiązany z innym przepisem oraz składniki jeśli nie są powiązane z innym przepisem.
                