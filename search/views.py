from django.shortcuts import render


def search(request):
    template_name = 'search.html'
    search = False

    context = {
        'search': search,
    }
    return render(request, template_name, context)
