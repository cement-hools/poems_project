from django.shortcuts import render, get_object_or_404
from .models import Poet, Poem

def index(request):
    template_name = 'poems/index.html'
    poets = Poet.objects.all()
    context = {
        'poets': poets,        
    }
    return render(request, template_name, context)


def poet_view(request, poet_pk):
    template_name = 'poems/poet.html'

    poet = get_object_or_404(Poet, pk=poet_pk)
    poems = poet.poem_set.all()
    divide_at = poems.count() // 2

    context = {
        'poet': poet,
        'poems': poet.poem_set.all(),
        'divide_at': divide_at
    }
    return render(request, template_name, context)


def poem_view(request, poem_pk):
    template_name = 'poems/poem.html'

    # Достает обьект из БД, если нет выдает ошибка 404
    poem = get_object_or_404(Poem, pk=poem_pk)
      # 
    # poem = Poem.objects.get(pk=poem_pk)
      # QuerySet список с методами
    # poem = Poem.objects.filter(pk=poem_pk).first()

    context = {
        'poem': poem,
    }
    return render(request, template_name, context)
