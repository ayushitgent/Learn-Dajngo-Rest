from django.http import HttpResponse,JsonResponse

def home_page(request):
    d = ["ankit",'ravi','uttam']
    
    return JsonResponse(d,safe=False)