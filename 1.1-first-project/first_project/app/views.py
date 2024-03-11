import os
from os import listdir
from os.path import isfile, join
from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render, reverse


def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    # здесь HTML шаблона нет,
    # возвращается просто текст
    current_time = (datetime.today().isoformat(sep=' ')).split('.')[0]
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    # Эта функция возвращает список имен всех файлов в рабочей директории.
    current_directory = os.getcwd()
    files_list= [f for f in listdir(current_directory) if isfile(join(current_directory, f))]
    files_names = f"Список файлов в рабочей директории: {', '.join(files_list)}"
    return HttpResponse(files_names)
    # raise NotImplemented

