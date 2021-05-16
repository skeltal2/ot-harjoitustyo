## Vaatimusmäärittely ##
### Sovelluksen tarkoitus ###
Sovellus on miinaharava-peli. Pelissä on pelikenttä, joka koostuu samannäköisistä neliöistä. Pelaaja voi "kaivaa" neliöitä paljasten sen sisällön. Jokainen neliö on joko tyhjä, miina tai numero. Jos neliö on tyhjä, se paljastaa kaikki viereiset neliöt, jotka ovat myös tyhjiä. Jos neliö on numero, se kertoo kuinka monessa neliön kahdeksassa viereisessä neliössä on miina. Jos pelaaja paljastaa miinan, peli on hävitty.

Pelaaja voi myös kaivamisen sijasta asettaa lipun kaivamattomalle neliölle. Jos kaikilla neliöillä jotka sisältävät miinan on lippu, pelaaja voittaa pelin.

### Perusversion toiminnallisuus ###
* Sovellus aukeaa päävalikkoon, jossa on pelaaja voi aloittaa uuden pelin, muuttaa pelin asetuksia, katsoa tuloksia tai poistua pelistä
* Uusi peli-vaihtoehto aloittaa uuden pelin
  * Pelaaja siirtyy toiseen näkymään, jossa on miinaharava-peli
  * Pelilaudan koko ja miinojen määrä riippuu vaikeustasosta
    * Helppo: 9 x 9 ruudukko, 10 miinaa
    * Keskitaso: 16 x 16 ruudukko, 40 miinaa
    * Vaikea: 30 x 16 ruudukko, 99 miinaa
  * Pelilaudan päällä on ajastin ja luku, joka kertoo kuinka monta miinaa kentällä on
  * Kun peli on loppu, pelaaja näkee kuinka paljon aikaa kului ja siirtyy takaisin päävalikkoon
* Pelaaja voi vaihtaa pelin vaikeustasoa
* Pelikenttä luodaan kun pelaaja paljastaa ensimmäisen neliön. Miinat sijoitetaan satunnaisesti kentälle ja jokainen neliö, joka on miinan vieressä muutetaan numeroksi. Ensimmäinen neliö, jonka pelaaja paljastaa on aina tyhjä neliö.
* Ennen pelin aloittamista pelaaja voi antaa nimen. Jos pelaaja on antanut nimen ja voittaa pelin, peliin käytetty aika tallennetaan.
* Tulokset vaihtoehto avaa näkymän, jossa pelaaja voi katsoa tuloksia
* Poistu pelistä-vaihtoehto sulkee sovelluksen

### Jatkokehitysideoita ###
* Pelaaja voi luoda oman vaikeustason asetuksissa
