from django.http import HttpResponse, JsonResponse


def teste(request):
    return HttpResponse("Teste Django")