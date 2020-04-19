import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from mid.auth_.models import MyUser


@csrf_exempt
def register(request):
    permission_classes = ()
    body = json.loads(request.body.decode('utf-8'))
    username = body.get('username')
    password = body.get('password')
    role = body.get('role')

    user = MyUser.objects.create_user(username=username)
    user.set_password(password)
    user.set_role(role)
    user.save()

    return JsonResponse({'message': f'{user.role} user with username {user.username} created'}, status=200)