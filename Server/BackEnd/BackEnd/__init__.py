from django.core.cache import cache
import requests

# set cache timeout
CACHE_TIMEOUT = 5
# initialize the url to fetch datas
HOST = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/"
# initializing the requset's urls
URLS = {'WORLD_DETAILS': HOST + "worldstat.php", 'IMAGES': HOST + "random_masks_usage_instructions.php",
        'LIST_COUNTRY': HOST + "affected.php", 'CASE_BY_COUNTRY': HOST + "cases_by_country.php"}

# headers with the host address and keys
HEADERS = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "87292e93c0mshcf4772b1bcfb281p19373djsn916de1527165"
}


# print(URLS['WORLD_DETAILS'])
# initializing the cache

def initialize_cache():
    for name in URLS:
        if name == 'IMAGES':
            for i in range(1, 4):
                cache.add(name + '_' + str(i), 'initial', CACHE_TIMEOUT)
        else:
            cache.add(name, 'initial', CACHE_TIMEOUT)


initialize_cache()
