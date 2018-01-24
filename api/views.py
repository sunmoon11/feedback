from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.models import User
from django.http import JsonResponse


# @api_view(['POST', ])
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        django_login(request, user)
        return JsonResponse({'success': True})
    else:
        return JsonResponse({'success': False})


# @api_view(['POST', ])
def register(request):
    account = User.objects.create_user(username=request.POST['username'],
                                       password=request.POST['password'])
    account.save()

    django_login(request, account)

    return JsonResponse({'success': True})
