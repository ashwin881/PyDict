from django.shortcuts import render
from bs4 import BeautifulSoup
import requests
import re

def home(request):
    return render(request,"base.html")

def finder(request):
    word = request.GET['word']
    meaning = requests.get('https://www.merriam-webster.com/dictionary/'+word)
    synonyms = requests.get('https://www.merriam-webster.com/thesaurus/'+word)
    if meaning:
        soup = BeautifulSoup(meaning.text, "lxml")
        meaning1 =[p.text[2:] for p in soup.find_all(class_="dtText")[:3]]
    else:
        word = 'Sorry '+ word + 'is not found in dictionary'
        meaning = ''
        meaning1 = ''
        
    if synonyms:
        soup2 = BeautifulSoup(synonyms.text, "lxml")
        synonyms1 =[p.text.replace("\n", "").strip() for p in soup2.find_all(class_="dt")[:2]]
    else:
        word = 'Sorry '+ word + 'is not found in dictionary'
        synonyms = ''
        synonyms1 = ''
    result ={
        'word':word,
        'meaning':meaning1,
        'thesaurus':synonyms1
        
    }
    return render(request,"word.html",{'results': result})
     

       
        