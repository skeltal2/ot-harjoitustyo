## Luokkakaavio:
![image](https://user-images.githubusercontent.com/77693693/116288587-55ba3180-a79a-11eb-9097-8e403c5f6c11.png)

## Sekvenssikaavio:
![image](https://user-images.githubusercontent.com/77693693/116299883-e6970a00-a7a6-11eb-9d39-b6fa6b2408bb.png)

Gameloop luokka kutsuu FieldGenerator luokaa arvoilla (x: 16, y: 16, mines: 40, tile_size: 36, first_click: (0, 0)). Luokan metodi generate() palauttaa 16x16 pelikentän (matriisin), jossa on 40 miinaa, ja yksikään miina ei ole neliön (0, 0) vieressä. Seuraavaksi Gameloop kutsuu Field luokkaa FieldGeneratorin luomalla pelikentällä, joka asettaa oikeat spritet pelikentän osoittamiin paikkoihin.
