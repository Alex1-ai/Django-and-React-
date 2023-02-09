from django.http import JsonResponse

# Create your views here.


def home(request):
    return JsonResponse({
        'info': "Admin",
        'name': "Chidi",
        'phone': "+233503168382",
        'whatsapp': "+2348067490562",

    })
