from bs4 import BeautifulSoup
import requests
import re
word = 'happiness'
meaning = requests.get('https://www.merriam-webster.com/dictionary/'+word)
synonyms = requests.get('https://www.merriam-webster.com/thesaurus/'+word)
if meaning:
    
    soup = BeautifulSoup(meaning.text, "lxml")
    meaning1 =[p.text[2:] for p in soup.find_all(class_="dtText")[:3]]
if synonyms:
    
    soup2 = BeautifulSoup(synonyms.text, "lxml")
    synonyms1 =[p.text.replace("\n", "").strip() for p in soup2.find_all(class_="dt")[:3]]

print(meaning1)
print()
print(synonyms1)
        