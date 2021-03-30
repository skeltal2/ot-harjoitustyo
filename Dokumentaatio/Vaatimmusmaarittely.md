### Vaatimusm��rittely ###
## Sovelluksen tarkoitus ##
Sovellus on miinaharava-peli. Peliss� on pelikentt�, joka koostuu samann�k�isist� neli�ist�. Pelaaja voi "kaivaa" neli�it� paljasten sen sis�ll�n. Jokainen neli� on joko tyhj�, miina tai numero. Numero kertoo kuinka monta miinaa neli�n vieress� on. Jos neli� on tyhj�, se paljastaa kaikki viereiset neli�t jotka ovat my�s tyhji�. Jos pelaaja "kaivaa" miinan, peli on h�vitty.
Pelaaja voi my�s kaivamisen sijasta asettaa lipun neli�lle. Jos kaikilla neli�ill�, jotka sis�lt�v�t miinan on lippu, pelaaja voittaa pelin.
## Perusversion toiminnallisuus ##
* Sovellus aukeaa p��valikkoon, jossa on pelaaja voi aloittaa uuden pelin, muuttaa pelin asetuksia, tai poistua pelist�
* Uusi peli-vaihtoehto aloittaa uuden pelin
  * Pelaaja siirtyy toiseen n�kym��n, jossa on pelilauta
  * Pelilauta on x \* y kokoinen ruudukko, joka koostuu tyhjist� neli�ist�
  * Pelilaudan p��ll� on ajastin ja luku, joka kertoo kuinka monta miinaa kent�ll� on
  * Kun peli on loppu, pelaaja n�kee kuinka paljon aikaa kului ja siirtyy takaisin p��valikkoon
* Asetukset-vaihtoehto siirt�� pelaajan n�kym��n, jossa pelaaja voi muuttaa pelin asetuksia
  * Pelaaja voi muuttaa pelikent�n kokoa muuttamalla x ja y arvoja
  * Pelaaja voi muuttaa kuinka monta miinaa kent�ll� on
* Poistu pelist�-vaihtoehto sulkee sovelluksen
* Pelikentt� luodaan kun pelaaja paljastaa ensimm�isen neli�n. Miinat sijoitetaan satunnaisesti kent�lle ja jokainen neli�, joka on miinan vieress� muutetaan numeroksi. Ensimm�inen neli�, jonka pelaaja paljastaa on aina tyhj� neli�.
## Jatkokehitysideoita ##
* Pelin p��ttyess� pelaaja voi antaa nimens� jonka j�lkeen pelin aika tallennetaan.
* P��valikossa on uusi vaihtoehto, jossa pelaaja voi katsoa eri kentt�kokojen parhaat ajat.