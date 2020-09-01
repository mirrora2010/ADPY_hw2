from pprint import pprint
import json
import wikipediaapi


wiki_wiki = wikipediaapi.Wikipedia('en')
# wiki_wiki = wikipediaapi.Wikipedia('ru')

def get_country_name():
    with open('countries.json', encoding='utf-8') as countries_info:
        country = json.load(countries_info)
        countries_names_list = []
        for item in country:
            countries_names_list.append(item['name']['official'])
    # pprint(countries_names_list)
    return countries_names_list


class CountryIterator:

    def __init__(self, start=0, end=len(get_country_name())-1):
        self.start = start  
        self.end = end  
        self.current = start
        self.country_list = get_country_name()

    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current > self.end:
            raise StopIteration
        self.link = self.get_link(self.country_list[self.current])
        return {self.country_list[self.current]: self.link}

    def get_link(self, country):

        try:
            page = wiki_wiki.page(country)
            print('...processing...')
            return page.fullurl
        except KeyError:
            return ('Seems no such page on Wikipedia. Create it!')
        

country_link = []
for item in CountryIterator():
    country_link.append(item)

with open('country_link.json', 'w', encoding='utf-8') as outfile:
    json.dump(country_link, outfile, ensure_ascii=False, indent=2)
print('Done! Please check your .json file')