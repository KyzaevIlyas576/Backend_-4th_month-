from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models


def book_list_view(request):
    if request.method == 'GET':
        query_books = models.Book.objects.all().order_by('-id')
        return render(request, 'book_list.html', {'book': query_books})
    

def book_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Book, id=id)
        return render(request, 'book_detail.html', {'book_id': book_id})


def message(request):   # решил оставить похожее сообщение
    return HttpResponse('Это мой второй проект на DJANGO')


def quote1(request):
    return HttpResponse('''
            «Отложите эту книгу и поразмышляйте пять минут над тем фактом, что все 
            великие религии были впервые проповеданы и долгое время практиковались в мире без хлороформа.»,
            — Клайв Стейплз Льюис, как ветеран Первой Мировой Войны, о вере и обеих мировых войнах (1940).
                        ''')


def quote2(request):
    return HttpResponse('''
            «Зло не способно создавать ничего нового; оно может лишь портить и разрушать то, что было изобретено или создано добрыми силами», 
            — фраза, приписываемая Джону Рональду Руэлу Толкину. Похожая, другая фраза изначально встречалась во «Властелине Колец».
                        ''')


def quote3(request):
    return HttpResponse('''
            «Если главная цель в жизни не количество прожитых лет, а честь и достоинство, то какая разница, когда умирать?», 
            —  Джордж Оруэлл (Эрик Артур Блэр), автор «1984».
                        ''')

# Create your views here.