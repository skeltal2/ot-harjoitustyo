# Miinaharava #
Sovellus on klassinen miinaharava-peli. Pelaajan tavoitteena on etsiä kaikki miinat pelikentältä käyttäen miinojen viereisissä neliöissä olevia numeroita.

## Dokumentaatio ##
[Vaatimusmäärittely](https://github.com/skeltal2/ot-harjoitustyo/blob/master/Dokumentaatio/vaatimmusmaarittely.md)

[Työaikakirjanpito](https://github.com/skeltal2/ot-harjoitustyo/blob/master/Dokumentaatio/tyoaika.md)

## Komentorivi ##
### Ohjeman suorittaminen ###
```bash
poetry run invoke start
```

### Testaus ###
```bash
poetry run invoke test
```

### Testien suorittaminen ###
```bash
poetry run invoke coverage
```

### Testikattavuus ###
```bash
poetry run invoke coverage-report
```

### Pylint testien suorittaminen ###
```bash
poetry run invoke lint
```
