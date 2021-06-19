# Detekce osob a vozidel pomocí TensorFlow Object Detection API

## Dataset

Na webu [bezpecnost.praha.eu](https://bezpecnost.praha.eu/mapy/kamery) jsou k dispozici záběry bezpečnostních kamer po celé Praze. Pro účely této semestrální práce jsem si vybral kameru, které se nachází [na křižovatce u Národního divadla](https://mapy.cz/s/cabanukoza). Během jejího výběru se mi zalíbil její záběr, který snímal část křižovatky a přilehlý přechod pro chodce.

Vytvořil jsem si proto [jednoduchou funkci](./images_fetcher/main.py), kterou jsem následně nasadil do Google Cloudu. Jedinou její činností je každou minutu stáhnout snímek z kamery, pojmenovat daný soubor aktuálním časem a uložit ho do Cloud Storage. Takto jsem sbíral snímky od 21. května až do 16. června. Nasbíral jsem více než 36 tisíc obrázků.

Několik dní po začátku snímání jsem při kontrole funkčnosti zjistil, že jsem si vybral kameru, která není statická. Její záběr se během období sbírání dat několikrát změnil. Proto nemohu dělat žádnou dlouhodobější analýzu, která by například srovnávala pohyb osob v jednotlivých dnech v týdnu. Dalším problémem, na který jsem narazil, byly občasné výpadky kamery. Někdy vypadla jen na minutu, jindy i na několik dní.

Zip s celým datasetem lze stáhnout [zde](https://vse-my.sharepoint.com/:u:/g/personal/hovp01_vse_cz/EWZGoaK7jbxEsKT12tRn87gBGdICTHcTGryvv2qo-DDXJA?e=6Oy0HR). Stačí ho rozbalit ve složce [`/dataset`](/dataset)

Abych mohl vybrat nejvhodnější období, ve kterém se neměnil záběr a nedocházelo k častým výpadkům, složil jsem ze snímků časosběrné video. Využil jsem k tomu nástroj FFmpeg. Bash skript, který se o vytvoření videa z jednotlivých snímků stará lze nalézt [zde](./dataset/generate_video.sh). Jeho součástí je i přidání textu s časem pořízení konkrétního snímku přímo do videa. Video bylo upscalováno na vyšší rozlišení než je rozlišení původních snímků. K tomuto kroku bylo přistoupeno kvůli YouTube kompresi, která je u videí s nižším rozlišením příliš agresivní.

Výsledné video je možné vidět zde:
[![Theatre timelapse](https://i.ytimg.com/vi/043zAO5q1bg/maxresdefault.jpg)](https://youtu.be/043zAO5q1bg "Theatre timelapse")
