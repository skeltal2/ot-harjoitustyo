# Käyttöohje

## Asentaminen
Kun peli ladataan ensimmäisen kerran, se asennetaan suorittamalla:
```bash
poetry install
```

Tämän jälkeen peli käynnistetään suorittamalla:
```bash
poetry run invoke start
```

## Päävalikko
![image](https://user-images.githubusercontent.com/77693693/118402399-775c5980-b672-11eb-8f32-1926d46d8d35.png)

Päävalikossa on 5 eri vaihtoehota:
 * Uusi peli
 * Vaikeusaste
 * Nimi
 * Tulokset
 * Poistu

### Uusi peli
Aloita uusi peli valitulla vaikeusasteella. Jos vaikeusastetta ei ole valittu peli alkaa keskitaso-vaikeusasteella.
![image](https://user-images.githubusercontent.com/77693693/118403056-52b5b100-b675-11eb-8b5f-ec27034e97d0.png)

Peliruudun yläreunassa näkyy kuinka monta lippua pelaaja voi asettaa ja kulunut aika. Pelaaja voi asetaa yhtä monta lippua, kuin kentällä on miinoja.

Pelaaja voi avata ruudun hiiren vasemmalla painikkeella. Pelaaja voi asettaa lipun hiiren oikealla painikkeella. Pelaaja voittaa pelin kun kaikilla avaamattomilla ruuduilla, joissa on miina on, lippu. Jos pelaaja avaa ruudun, jossa on miina, peli päättyy.

### Vaikeusaste
Valitse pelin vaikeusaste kolmesta eri vaihtoehdosta.
 * Helppo (9 x 9 ruudukko, 10 miinaa)
 * Keskitaso (16 x 16 ruudukko, 40 miinaa)
 * Vaikea (30 x 16 ruudukko, 99 miinaa)

### Nimi
Valitse nimi, jolla voitetun pelin aika tallennetaan. Jos nimi jätetään tyhjäksi, aikaa ei tallenneta.

### Tulokset
![image](https://user-images.githubusercontent.com/77693693/118402843-5f85d500-b674-11eb-9994-a5c4ffa90aef.png)

Avaa toinen näkymä, jossa voi katsoa parhaita tuloksia. Tulokset on jaettu kolmeen eri taulukkoon vaikeusasteen perusteella. Jokaisessa taulukossa on 10 parasta aikaa ja jokaisen ajan saavuttanut nimi. Tulokset näymästä voi siirtyä takaisin päävalikkoon painamalla takaisin-painiketta ikkunan alaosassa.

### Poistu
Vaihtoehto sulkee ohjelman. Ohjelman voi myös sulkea milloin tahansa painamalla X-painiketta.
