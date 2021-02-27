# Teams Bot

Teams Bot je python program na automatické připojení na hodiny provozované na Microsoft Teams a sdílenými přes Bakaláře.

## Instalace
### Příprava
Hodíme "teams_bot.py" do složky společně s textovými dokumenty "username.txt", "password.txt" a "school.txt" kam vložíme udaje na bakaláře a odkaz na web bakalářů vaší školy (např. "skola.cz").
### Získání chromedriveru
Abychom programu umožnili spustit a ovládat náš prohlížeč, musíme si stáhnout tzv. ovladač, nejdřív si zjistíme verzi Chromu následovně:

```
V prohlížeči Chrome vpravo nahoře otevřete nabídku Přizpůsobit (tři tečky nad sebou)
Zvolte „Nápověda“ a následně „O aplikaci Google Chrome“
```
Poté [zde](https://chromedriver.chromium.org/downloads) stáheneme chromedriver odpovídající verzi našeho chromu a vložíme ho do složky ke scriptu.
### Instalace potřebných knihoven
Aby mohl program správně fungovat, je potřeba také nainstalovat potřebné python knihovny následovně.
```
pip3 install -r requirements.txt
```
## Použití
```
python3 teams_bot.py
```
Program se poté automaticky přihlásí na bakaláře, vezme si odkaz a počká na hodinu kam se poté připojí.
