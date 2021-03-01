################################################################
## Fuck online classes, never gonna learn anything from them. ##
################################################################

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from datetime import datetime as dtt
import datetime
import requests
import ctypes
import locale
import platform
import json
from requests_html import HTMLSession
import lxml.html
import re
sys = platform.system()
## CLEAN FUNCTION ##
def clean():
  if sys == "Windows":
    os.system("cls")
  elif sys == "Linux":
    os.system("clear")

clean()

print("""
  _____                          ____        _   
 |_   _|__  __ _ _ __ ___  ___  | __ )  ___ | |_ 
   | |/ _ \/ _` | '_ ` _ \/ __| |  _ \ / _ \| __|
   | |  __/ (_| | | | | | \__ \ | |_) | (_) | |_ 
   |_|\___|\__,_|_| |_| |_|___/ |____/ \___/ \__|
                    version 1.3 made by NayKeYY

""")

time.sleep(1)
# check if using supported OS
if sys == "Windows":
  msg = "[X] Verze pro: " + sys + " (Detekováno automaticky..)"
elif sys == "Linux":
  msg = "[X] Verze pro: " + sys + " (Detekováno automaticky..)"
else:
  print("[X] Používáš nepodporovaný OS! TeamsBot podporuje Windows A Linux..")
  exit()

if sys == "Windows":
  dir = os.path.dirname(os.path.realpath(__file__)) + '\chromedriver.exe'
elif sys == "Linux":
  dir = os.getcwd() + "/chromedriver"
print(msg)
time.sleep(2)
clean()


try:
  j = open("username.txt", "r")
except:
  print('[X] Nebyl nalezen soubor "username.txt", vytvoř ho v adresáři kde máš tento script a vlož do něj jméno na bakaláře.')
  exit()
try:
  h = open("password.txt", "r")
except:
  print('[X] Nebyl nalezen soubor "password.txt", vytvoř ho v adresáři kde máš tento script a vlož do něj heslo na bakaláře.')
  exit()
try:
  s = open("school.txt", "r")
except:
  print('[X] Nebyl nalezen soubor "school.txt", vytvoř ho v adresáři kde máš tento script a vlož do něj odkaz na školní web bakalářů.')
  exit()

skola = s.readline()
s.close()
baka_url = "https://" + skola + "/bakaweb/Login"
login_user = j.readline()
login_pass = h.readline()
j.close()
h.close()
login = {"username": login_user, "password": login_pass, "returlUrl": "https://" + skola + "/bakaweb/Collaboration/OnlineMeeting/MeetingsOverview", "Login":""}

session = HTMLSession()
p1 = session.post(baka_url, data=login)
print("-------------------------------------")
print("")
print("[X] Synchronizuji hodiny z bakalářů..")
print("")
print("-------------------------------------")

if p1.url != "https://" + skola + "/bakaweb/dashboard":
  print("[X] Nepodařilo se připojit k bakalářům..")
  exit()
time.sleep(2)
clean()
g1 = session.get("https://" + skola + "/bakaweb/Collaboration/OnlineMeeting/MeetingsOverview")

doc = lxml.html.fromstring(g1.content)
full = doc.xpath('/html/head/script[39]/text()')[0]
full = str(re.findall(r'meetingsData = .*;', full)).split("=")[1][:-3]
full =  '{"hodiny":' + full + '}'
full = json.loads(full)
date_format = '%d.%m.%Y-%H:%M'
hodiny_list = []
for hodiny in full["hodiny"]:
  start_data = (hodiny["MeetingStart"])
  hodiny_list.append(start_data)

pocet_hodin = len(hodiny_list)
# kontroluje jestli je v seznamu nejaka hodina
if pocet_hodin == 0:
    print("[X] Nepodařilo se importovat hodiny z bakalářů, nejspíš tam žádné nejsou.")
    print("")
    exit()

hodiny_list.sort()
cas_nejblizsi_hodiny = hodiny_list[0]

d = dtt.fromisoformat(cas_nejblizsi_hodiny)
datum_nejblizsi_hodiny = d.strftime('%d.%m.%Y - %H:%M')
rok = int(d.strftime("%Y"))
mesic = int(d.strftime("%m"))
den = int(d.strftime("%d"))
hodina = int(d.strftime("%H")) - 1
minuta = int(d.strftime("%M")) + 55

# Funkce na ziskani ID nejblizsi hodiny ktera mi trvala tak mesic nez jsem to dopici udelal vsechno jo
for hodiny in full['hodiny']:
    if hodiny['MeetingStart'] == cas_nejblizsi_hodiny:
      id_nejblizsi_hodiny = str(hodiny['Id'])


r1 = session.get("https://" + skola + "/bakaweb/Collaboration/OnlineMeeting/Detail/" + id_nejblizsi_hodiny + "?_=1609555900854")
dzejsn = json.loads(r1.text)
url = dzejsn["data"]["JoinMeetingUrl"]
nazev_hodiny = dzejsn["data"]["Title"]

print("-------------------------------------")
print("")
print("[X] Byla nalezena nejnovější hodina z bakalářů!:")
print("")
print('[X] Název hodiny: "' + nazev_hodiny + '"' + " | Začíná: " + datum_nejblizsi_hodiny + " |")
print("")
print("-------------------------------------")
print("")
inn = input("[X] Použít toto nastavení? [Y/N]: ")
if inn != "Y":
  clean()
  exit()
clean()
print("-------------------------------------")
print("")

## TIMING ##
print("[X] Čekám do " + datum_nejblizsi_hodiny + " na hodinu!")
print("")
print("-------------------------------------")
target = datetime.datetime(rok,mesic,den,hodina,minuta)
def sleep_until(target):
    now = dtt.now()
    delta = target - now

    if delta > datetime.timedelta(0):
        time.sleep(delta.total_seconds())
        return True

sleep_until(target)

clean()
### CHECK OS LANGUAGE ### 
if sys == "Windows":
  windll = ctypes.windll.kernel32
  lang = (locale.windows_locale[ windll.GetUserDefaultUILanguage() ])
  if lang == "cs_CZ":
    prefix = "(Host)"
  else:
    prefix = "(Guest)"
elif sys == "Linux":
  prefix = "(Guest)"

#
jmeno = "SEM VLOZ JMENO NA TEAMS " + prefix
#
### PRIPOJENI ###
# Chrome oprávnění (mikrofon, webkamera..)
opt = Options()
opt.add_argument("start-maximized")
opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 2, 
    "profile.default_content_setting_values.media_stream_camera": 2,
    "profile.default_content_setting_values.geolocation": 2, 
    "profile.default_content_setting_values.notifications": 2 
  })

driver = webdriver.Chrome(options=opt, executable_path=dir)
driver.get(url)
driver.maximize_window()

# klikne na "pokračovat v tomto prohlížeči."
if sys == "Windows":
  driver.find_element_by_xpath("""//*[@id="buttonsbox"]/button[2]""").click()
elif sys == "Linux":
  driver.find_element_by_xpath("""//*[@id="buttonsbox"]/button[1]""").click()
# počká 6 vteřin na redirect na poslední stránku.
time.sleep(6)
# klikne na "pokračovat bez zvuku a videa."
driver.find_element_by_xpath("""//*[@id="ngdialog1"]/div[2]/div/div/div/div[1]/div/div/div[2]/div/button""").click()
# Inputne jmeno.
nameinput = driver.find_element_by_xpath("""//*[@id="username"]""")
nameinput.send_keys(jmeno)
# Klikne na připojit.
driver.find_element_by_xpath("""//*[@id="page-content-wrapper"]/div[1]/div/calling-pre-join-screen/div/div/div[2]/div[1]/div[2]/div/div/section/div[1]/div/div[2]/button""").click()
