import urllib.request
from bs4 import BeautifulSoup


class CategoryDeepSearch:

    def __init__(self, name):
        self.name = name

    def iab_cats(self):
        url = 'https: // support.aerserv.com / hc / en - us / articles / 207148516 - List - of - IAB - Categories'
        page = urllib.request.urlopen(url)
        soup = BeautifulSoup(page, 'html.parser')
        table = soup.find('table')
        titles = table.findAll(attrs={'scope': 'row'})

        category_href = [row.findAll('tr') for row in titles]
        clean_links = [i for i in category_href]

        return clean_links

name = input('Enter a category: ')
category = CategoryDeepSearch(name)
print(category.iab_cats())


# Need to change the URL encoding to be parsed better