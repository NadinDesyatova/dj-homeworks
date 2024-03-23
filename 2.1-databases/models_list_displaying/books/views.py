from datetime import datetime
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from books.models import Book


def index(request):
    return redirect('books')


def get_books_list() -> list:
    books_objects = Book.objects.all()
    books: list = [
        {
            'name': b.name,
            'author': b.author,
            'pub_date': b.pub_date,
        }
        for b in books_objects
    ]

    return books


def get_books_by_pub_date() -> list:
    books: list = get_books_list()
    books_dict: dict = {}
    for book in books:
        if book['pub_date'] not in books_dict:
            books_dict[book['pub_date']] = []
            books_dict[book['pub_date']].append(book)

        elif book['pub_date'] in books_dict:
            books_dict[book['pub_date']].append(book)

    new_books_list: list = []
    for key, value in books_dict.items():
        new_books_list.append(
            {
                'pub_date': str(key),
                'books': [
                    {
                        'name': b['name'],
                        'author': b['author'],
                        'pub_date': str(b['pub_date']),
                    }
                    for b in value
                ]
            }
        )
    new_books_list.sort(key=lambda b: datetime.strptime(b.get('pub_date'), '%Y-%m-%d'))

    return new_books_list


def books_view(request):
    template = 'books/books_list.html'
    books = get_books_list()
    for book in books:
        book['pub_date'] = book['pub_date'].strftime('%Y-%m-%d')
    context = {
        'books': books,
    }
    return render(request, template, context)


def books_on_required_day(request, required_pub_date):
    template = 'books/books_on_required_date.html'
    books_list_by_pub_date = get_books_by_pub_date()
    paginator = Paginator(books_list_by_pub_date, 1)
    page = paginator.get_page(1)
    adjacent_pages: dict = {}
    for i, element in enumerate(books_list_by_pub_date):
        if element['pub_date'] == required_pub_date:
            page = paginator.get_page(i + 1)
            if i == 0:
                adjacent_pages = {
                    'next': books_list_by_pub_date[i + 1]['pub_date']
                }
            elif i == len(books_list_by_pub_date) - 1:
                adjacent_pages = {
                    'previous': books_list_by_pub_date[i - 1]['pub_date'],
                }
            else:
                adjacent_pages = {
                    'previous': books_list_by_pub_date[i - 1]['pub_date'],
                    'next': books_list_by_pub_date[i + 1]['pub_date']
                }

    context = {
        'adjacent_pages': adjacent_pages,
        'page': page,
    }
    return render(request, template, context)