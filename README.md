# Election_scraper

Tento program slouží k automatickému stahování výsledků voleb do csv souboru pro vybranou obec v České republice. Program pracuje s daty, která jsou získávána z oficiálních volebních stránek Českého statistického úřadu.

Jak program funguje:

Program načte URL stránky s výsledky voleb a zkontroluje zadané argumenty.
Program stáhne potřebná data z webových stránek a uloží je do csv souboru s názvem 'election_results.csv'.
Výsledky voleb jsou uloženy pro každou politickou stranu v každé obci, kde se volby konaly. V souboru jsou zahrnuty následující údaje pro každou obec: název obce, počet voličů, počet platných hlasů, počet platných obálek, počet hlasů pro každou politickou stranu.
Jak program použít:

Program se spouští z příkazové řádky s následujícími dvěma argumenty:
URL adresa volebních výsledků pro zvolenou obec (adresu lze získat ze stránek Českého statistického úřadu)
název csv souboru, kam se výsledky uloží
Po spuštění programu budou výsledky automaticky stahovány a uloženy do zvoleného csv souboru.

Potřebné knihovny:

Použité knihovny, potřebné pro správné fungování programu najdete v přiloženém soubou requirements.txt.
Pro instalaci knihoven je potřeba nové virtuální prostředí a v něm nejdříve ověřit verzi manažera a následně knihovny nainstalovat pomocí:

$ pip3 --version # ověření verze manažera

$ pip3 install -r requirements.txt # instalace knihoven

Spouštění programu:

Program se spouští pomocí dvou argumentů:
1.) URL požadovaného okresu z webu volby.cz
2.) názvu .csv souboru, do kterého se uloží výsledky

python election_results.py 'URL adresa volebních výsledků' 'název csv souboru pro uložení výsledků'

Příklad spuštění programu:
python election_results.py 'https://www.volby.cz/pls/ps2017nss/ps311?xjazyk=CZ&xkraj=10&xobec=554782&xvyber=6203' 'election_results.csv'

Ukázka projektu:

Výsledky hlasování pro okres Brno-venkov

Použité argumenty:
1.) https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203
2.) election_results.csv

Spuštění programu v terminálu:

python election_scraper.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203" "election_results.csv"

Průběh stahování v případě správného zadání argumentů:

Stahuji data z vybraného url: https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=11&xnumnuts=6203
Ukládám data do election_results.csv
Data byla uložena. Ukončuji program

Ukázka výstupu:

Code,Location,Registered,Envelopers,Valid... 582794,Babice nad Svitavou,925,660,655,109,1,2,43,0,53,31,7,3,10,0,0,14,0,39,129,0,3,69,0,2,1,1,58 582808,Babice u Rosic,553,353,353,32,0,0,18,1,27,30,5,1,6,0,2,37,0,13,93,0,1,25,5,4,1,49,0

V případě špatně zadaných argumentů program vypíše:

a. Program potřebuje 2 argumenty! URL a složku csv. Ukončuji program.
b. První argument nebyl správně zadán. Ukončuji program.
c. Druhý argument nebyl správně zadán. Ukončuji program.
