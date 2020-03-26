from django.shortcuts import render
from django.http import HttpResponse
from . import models

from bs4 import BeautifulSoup as soup 
import requests

# Create your views here.

url = 'https://bleacherreport.com/nba'
url1 = 'https://bleacherreport.com/nfl'
url2 = 'https://www.gamesradar.com/uk/play/'
url3 = 'https://www.gameinformer.com/reviews'
url4 = 'https://www.indiewire.com/'

def home(request):
    return render(request, 'base.html')

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search,blank=True,null=True)

    if search == "bleacher nba":
        page_url = requests.get(url)
        pagesoup = soup(page_url.text, 'html.parser')
        main_class = pagesoup.find_all('a', {'class': 'atom articleTitle'})
    
        links = []
        text_links = []
        text_revised = []

        for i in main_class:
            links.append(i['href'])
    
        for i in links:
            text_links.append(i[44:])
    
        for i in text_links:
            text_revised.append(i.replace("-", " "))

        fou = zip(links, text_revised)

        stuff_frontend = {
            'fou': fou,
        }
        return render(request, 'webscraping/new_search.html', stuff_frontend)

    elif search == "bleacher nfl":
        page_url = requests.get(url1)
        pagesoup = soup(page_url.text, 'html.parser')
        main_class = pagesoup.find_all('a', {'class': 'atom articleTitle'})
    
        links = []
        text_links = []
        text_revised = []

        for i in main_class:
            links.append(i['href'])
    
        for i in links:
            text_links.append(i[44:])
        
        for i in text_links:
            text_revised.append(i.replace("-", " "))
            
        brute = zip(links, text_revised)

        stuff_frontend = {
            'brute': brute,
        }
        return render(request, 'webscraping/new_search.html', stuff_frontend)

    elif search == 'gamesradar':
        page_url = requests.get(url2)
        pagesoup = soup(page_url.text, 'html.parser')
        main_class = pagesoup.select('.listingResult a')

        links = []
        text_links = []
        text_revised = []

        for i in main_class:
            links.append(i['href'])

        for i in links:
            if i == 'javascript:void(0)':
                links.remove(i)

        for i in links:
            text_links.append(i[30:-1])
        
        for i in text_links:
            text_revised.append(i.replace("-", " "))
        
        radar = zip(links, text_revised)
        
        stuff_frontend = {
            'radar': radar,
        }
        return render(request, 'webscraping/new_search.html', stuff_frontend)

    elif search == 'gameinformer reviews':
        page_url = requests.get(url3)
        pagesoup = soup(page_url.text, 'html.parser')
        main_class = pagesoup.select('.teaser-right-wrapper a')

        links = []
        text_links = []
        text_revised = []

        for i in main_class:
            if i['href'][:6] == '/user/':
                main_class.remove(i)

        a = 'https://www.gameinformer.com'

        for i in main_class:
            links.append(a+i['href'])

        for i in links:
            dummy = i.split('/')
            text_links.append(dummy[-1])

        for i in text_links:
            text_revised.append(i.replace("-", " "))

        reviews = zip(links, text_revised)

        stuff_frontend = {
            'reviews': reviews,
        }
        return render(request, 'webscraping/new_search.html', stuff_frontend)

    elif search == 'indie wire feed':
        page_url = requests.get(url4)
        pagesoup = soup(page_url.text, 'html.parser')
        main_class = pagesoup.select('.o-story__content a')

        links = []
        text_links = []
        text_revised = []

        for i in main_class:
            links.append(i['href'])

        for i in links:
            if i[:33] == 'https://www.indiewire.com/c/film/':
                links.remove(i)
            elif i[:35] == 'https://www.indiewire.com/c/awards/':
                links.remove(i)
            elif i[:39] == 'https://www.indiewire.com/c/television/':
                links.remove(i)

        for i in links:
            if i[:33] == 'https://www.indiewire.com/author/':
                links.remove(i)
        
        for i in links:
            dummy = i.split('/')
            text_links.append(dummy[-2])
        
        for i in text_links:
            text_revised.append(i.replace("-", " "))
        
        text_revised2 = []
        for i in text_revised:
            text_revised2.append(i[:-10])
        
        indie = zip(links, text_revised2)

        stuff_frontend = {
            'indie': indie,
        }
        return render(request, 'webscraping/new_search.html', stuff_frontend)

    else:
        search1 = "Enter 'bleacher nba'"
        search2 = "Enter 'bleacher nfl'"
        search3 = "Enter 'gamesradar'"
        search4 = "Enter 'gameinformer reviews'"
        search5 = "Enter 'indie wire feed'"
        stuff_frontend = {
            'search1': search1,
            'search2': search2,
            'search3': search3,
            'search4': search4,
            'search5': search5,
        }   
        return render(request, 'webscraping/new_search.html', stuff_frontend)