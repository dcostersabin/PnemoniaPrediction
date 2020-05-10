from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.core.cache import cache
from BackEnd.cacheUpdater import updater
from django.http import HttpResponse


@api_view()
def index(request):
    check_cache = cache.get('WORLD_DETAILS', 'has_expired')
    if check_cache == 'has_expired' or check_cache == 'initial':
        # updating the cache content
        updater.updater('WORLD_DETAILS')
    response = cache.get('WORLD_DETAILS').json()
    return Response(response)


@api_view()
def images(request):
    check_cache = cache.get('IMAGES_1', 'has_expired')
    if check_cache == 'has_expired' or check_cache == 'initial':
        # updating the cache content
        updater.updater('IMAGES')
    response = {'image_1': cache.get('IMAGES_1').text,
                'image_2': cache.get('IMAGES_2').text,
                'image_3': cache.get('IMAGES_3').text,
                }
    return Response(response)


@api_view()
def country_status(request):
    check_cache = cache.get('CASE_BY_COUNTRY', 'has_expired')
    if check_cache == 'has_expired' or check_cache == 'initial':
        # updating the cache content
        updater.updater('CASE_BY_COUNTRY')
    response = cache.get('CASE_BY_COUNTRY').json()
    return Response(response['countries_stat'])


@api_view()
def list_country(request):
    check_cache = cache.get('LIST_COUNTRY', 'has_expired')
    if check_cache == 'has_expired' or check_cache == 'initial':
        # updating the cache content
        updater.updater('LIST_COUNTRY')
    response = cache.get('LIST_COUNTRY').json()
    return Response(response['affected_countries'])


