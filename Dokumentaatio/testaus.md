# Testausdokumentti
Ohjelma on testattu yksikkötestien avulla

### Pelilogiikka
Pelilogiikkaa tapahtuu `gameloop` luokassa ja sitä testaa `TestGameloop` testiluokka. Testiluokka alustetaan luomalla Gameloop-olio, jolla ei ole pygame-ikkunaa.
Testit testaavat `_open_tile()`, `_flag()` ja `_game_state()` funktioita valitsemalla satunnaisen ruudun Gameloop-olion luomasta _sprite groupista_ ja kutsumalla funktioita tämän neliön kordinaateilla.
Lopuksi testit katsovat, että _spriten_ kuva asetettiin oikein.

### Field- ja tile-olioit
Field-oliota testataan vain yhdellä testillä `TestField` luokassa, joka varmistaa, että `_initialize_sprites()` alustetaan oikein. Testi alustetaan luomalla 3 x 3 ruudukko, jonka keskellä on yksi miina. Testi varmistaa, että ruuduilla on oikea tyyli.

Tile-olioita testataan testaamalla `click()`, `flag()` ja `unflag()` funktioita `TestTile` luokassa. Testit alustetaan luomalla tile-olio, jonka tyyli on miina (-1). `flag()` ja `unflag()` testit kokeilevat lipun asettamista ja varmistavat, että ruudun _sprite_ muuttuu oikein.
`click()` funktiota kokeillaan kaikilla mahdollisilla ja väärällä tile-olion muodoilla. Testi varmistaa, että olion tyyli asettuu oikein.

### Generaattori
`FieldGenerator` luokkaa testaa `TestFieldGenerator` luokka. Testiluokka varmistaa, että `generate()` funktio luo oikean matriisin ja asettaa oikean määrän miinoja.

### Testauskattavuus
Käyttöliittymää mukaanottamatta yksikkötestien kattavuus on 77%.

![image](https://user-images.githubusercontent.com/77693693/118406062-6f58e580-b683-11eb-974c-e3bade17199b.png)

_gameloop.py_ tiedoston kattavuus on alhainen, koska  `_start()`, `_events()` ja `_render()` funktioita ei testata. Funktiot tarvitsevat pygame ikkunan toimiakseen, joten niitä ei voi testata yksikkötestien avulla.
Luokan muut funktiot hallitsevat pelkästään pelilogiikkaa, joten niitä voidaan testata ilman ikkunaa.
