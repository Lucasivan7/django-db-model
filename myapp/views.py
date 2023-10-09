from django.http import HttpResponse
# Create your views here.
def hello(request):
    return HttpResponse("Holaaaaa")

def about(request):
    return HttpResponse("Sobre Nosotros")