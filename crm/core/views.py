from django.http import HttpResponse


def alive(request):
    return HttpResponse('ok')
