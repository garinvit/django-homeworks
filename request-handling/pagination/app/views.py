from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.conf import settings
from django.core.paginator import Paginator
from urllib.parse import urlencode, quote_plus
import csv

def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    with open(settings.BUS_STATION_CSV, 'r', encoding='cp1251') as csv_file:
        reader = csv.DictReader(csv_file)
        paginator = Paginator(list(reader), 15)
        current_page = request.GET.get('page', 1)
        bus_stations = paginator.get_page(current_page)
        prev_page, next_page = None, None
        if bus_stations.has_previous():
            prev_page = '?' + urlencode({'page': bus_stations.previous_page_number()}, quote_via=quote_plus)
        if bus_stations.has_next():
            next_page = '?' + urlencode({'page': bus_stations.next_page_number()}, quote_via=quote_plus)
        return render_to_response('index.html', context={
            'bus_stations': bus_stations,
            'current_page': current_page,
            'prev_page_url': prev_page,
            'next_page_url': next_page,
        })
