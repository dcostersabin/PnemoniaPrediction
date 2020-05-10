from django.core.cache import cache
import requests

# method
__METHOD = "GET"
# set cache timeout
__CACHE_TIMEOUT = 120
# initialize the url to fetch datas
__HOST = "https://coronavirus-monitor.p.rapidapi.com/coronavirus/"
# initializing the requset's urls
__URLS = {'WORLD_DETAILS': __HOST + "worldstat.php", 'IMAGES': __HOST + "random_masks_usage_instructions.php",
          'LIST_COUNTRY': __HOST + "affected.php", 'CASE_BY_COUNTRY': __HOST + "cases_by_country.php"}

# headers with the host address and keys
# replace x-rapidapi-key with our key

__HEADERS = {
    'x-rapidapi-host': "coronavirus-monitor.p.rapidapi.com",
    'x-rapidapi-key': "insert your key here"
}


def updater(name):
    if name == 'IMAGES':
        for i in range(1, 4):
            response = requests.request(method=__METHOD, url=str(__URLS[str(name)]), headers=__HEADERS)
            cache.set(str(name) + '_' + str(i), response, __CACHE_TIMEOUT)
    else:
        response = requests.request(method=__METHOD, url=str(__URLS[str(name)]), headers=__HEADERS)
        cache.set(str(name), response, __CACHE_TIMEOUT)
