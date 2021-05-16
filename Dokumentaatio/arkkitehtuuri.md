# Arkkitehtuurikuvaus

## Rakenne
![image](https://user-images.githubusercontent.com/77693693/118404117-323c2580-b67a-11eb-870d-a47eaeebc5a8.png)

Pelin koodi on kahdessa eri kansiosa: _game_ ja _ui_. _Ui_ kansiossa on käyttöliittymään liittyvä koodi, ja _game_ kansiossa peli logiikkaan ja pelin piirtämiseen liittyvä koodi. _Assets_ kansiossa on kuvat, joita pelin spritet käyttävät. _Database_ kansiossa on tietokanta, johon tallennetaan voitettujen pelien ajat. Tietokanta luodaan vasta kun peli suoritetaan ensimmäisen kerran.

## Käyttöliittymä

Käyttöliittymässä on kaksi eri näkymää; päävälikko ja tulokset, jotka ovat toteutettu kahtena luokkana: _mainmenu_ ja _high_scores_. 

Päävalikko on aina aktiivisena, kun käyttäjä haluaa nähdä tulokset näkymän, päävalikko siirretään taustalle ja uusi _high_scores_ näkymä luodaan. Kun käyttäjä haluaa siirtyä takaisin päävalikkoon, _high_scores_ näkymä tuhotaan ja _mainmenu_ tuodaan takaisin esille.

## Tietokanta
Voitetun pelin päätyttyä pelaajan aika ja nimi tallennetaan `scores.db` tiedostoon. Tiedosto luodaan, kun käyttäjä käynnistää pelin tai katsoo tuloksia ensimmäisen kerran. Tietokantaan luodaan yksi taulukko _scores_. 

| id | score | mode | name |
|:--:|:-----:|:----:|:----:|

Taulukossa on neljä saraketta. _Score_ sarakkeessa on pelaajan käyttämä aika millisekuntteina, _mode_ sarakkeessa on pelin vaikeusaste (1, 2 tai 3) ja _name_ sarakkeessa on pelaajan nimi.

Jos pelaaja ei anna nimeä, pelin tulosta ei tallenneta.

## Luokkakaavio
Luokkien riippuvuudet toisistaan:
![image](https://user-images.githubusercontent.com/77693693/118407818-19883b80-b68b-11eb-9d68-213ec44bb382.png)

## Sekvenssikaavio
![image](https://user-images.githubusercontent.com/77693693/116299883-e6970a00-a7a6-11eb-9d39-b6fa6b2408bb.png)

Gameloop luokka kutsuu FieldGenerator luokaa arvoilla (x: 16, y: 16, mines: 40, tile_size: 36, first_click: (0, 0)). Luokan metodi generate() palauttaa 16x16 pelikentän (matriisin), jossa on 40 miinaa, ja yksikään miina ei ole neliön (0, 0) vieressä. Seuraavaksi Gameloop kutsuu Field luokkaa FieldGeneratorin luomalla pelikentällä, joka asettaa oikeat spritet pelikentän osoittamiin paikkoihin.
