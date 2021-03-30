### Vaatimusmäärittely ###
## Sovelluksen tarkoitus ##
Sovellus on miinaharava-peli. Pelissä on pelikenttä, joka koostuu samannäköisistä neliöistä. Pelaaja voi "kaivaa" neliöitä paljasten sen sisällön. Jokainen neliö on joko tyhjä, miina tai numero. Numero kertoo kuinka monta miinaa neliön vieressä on. Jos neliö on tyhjä, se paljastaa kaikki viereiset neliöt jotka ovat myös tyhjiä. Jos pelaaja "kaivaa" miinan, peli on hävitty.
Pelaaja voi myös kaivamisen sijasta asettaa lipun neliölle. Jos kaikilla neliöillä, jotka sisältävät miinan on lippu, pelaaja voittaa pelin.
## Perusversion toiminnallisuus ##
* Sovellus aukeaa päävalikkoon, jossa on pelaaja voi aloittaa uuden pelin, muuttaa pelin asetuksia, tai poistua pelistä
* Uusi peli-vaihtoehto aloittaa uuden pelin
  * Pelaaja siirtyy toiseen näkymään, jossa on pelilauta
  * Pelilauta on x \* y kokoinen ruudukko, joka koostuu tyhjistä neliöistä
  * Pelilaudan päällä on ajastin ja luku, joka kertoo kuinka monta miinaa kentällä on
  * Kun peli on loppu, pelaaja näkee kuinka paljon aikaa kului ja siirtyy takaisin päävalikkoon
* Asetukset-vaihtoehto siirtää pelaajan näkymään, jossa pelaaja voi muuttaa pelin asetuksia
  * Pelaaja voi muuttaa pelikentän kokoa muuttamalla x ja y arvoja
  * Pelaaja voi muuttaa kuinka monta miinaa kentällä on
* Poistu pelistä-vaihtoehto sulkee sovelluksen
* Pelikenttä luodaan kun pelaaja paljastaa ensimmäisen neliön. Miinat sijoitetaan satunnaisesti kentälle ja jokainen neliö, joka on miinan vieressä muutetaan numeroksi. Ensimmäinen neliö, jonka pelaaja paljastaa on aina tyhjä neliö.
## Jatkokehitysideoita ##
* Pelin päättyessä pelaaja voi antaa nimensä jonka jälkeen pelin aika tallennetaan.
* Päävalikossa on uusi vaihtoehto, jossa pelaaja voi katsoa eri kenttäkokojen parhaat ajat.