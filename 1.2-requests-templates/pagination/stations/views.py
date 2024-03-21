import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from django.conf import settings


bus_stations_list: list = []
with open(settings.BUS_STATION_CSV, encoding='utf-8') as f:
    reader = list(csv.DictReader(f, delimiter=','))
    for row in reader:
        bus_stations_list.append({
            'Name': row.get('StationName'),
            'Street': row.get('Street'),
            'District': row.get('District')
        })


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    # получает текущую страницу со списком станций и передает ее в контекст
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(bus_stations_list, 10)
    page = paginator.get_page(page_number)
    context = {
        'bus_stations': page,
        'page': page
    }
    return render(request, 'stations/index.html', context)
