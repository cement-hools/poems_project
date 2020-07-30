from django.shortcuts import render


def index(request):
    template_name = 'index.html'

    context = {
    }
    return render(request, template_name, context)


def poet_view(request, poet_pk):
    template_name = 'poet.html'

    context = {
    }
    return render(request, template_name, context)


def poem_view(request, poem_pk):
    template_name = 'poem.html'

    context = {
    }
    return render(request, template_name, context)
