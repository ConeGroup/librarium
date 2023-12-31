import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login as auth_login
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.models import User

@csrf_exempt
def registerFlutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        username = data["username"]
        email = data["email"]
        password1 = data["password1"]
        password2 = data["password2"]

        if User.objects.filter(username=username).exists():
            return JsonResponse({"status": "isTaken"}, status=403)

        newUser = User.objects.create_user(
            username = username, 
            email = email,
            password = password1,
        )
        
        newUser.save()
        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)

@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            auth_login(request, user)
            # Status login sukses.
            return JsonResponse({
                "username": user.username,
                "status": True,
                'email': user.email,
                "message": "Login succeed!"
                # Tambahkan data lainnya jika ingin mengirim data ke Flutter.
            }, status=200)
        else:
            return JsonResponse({
                "status": False,
                "message": "Login failed, deactivating account."
            }, status=401)

    else:
        return JsonResponse({
            "status": False,
            "message": "Login failed, wrong username or password."
        }, status=401)

@csrf_exempt
def logout(request):
    username = request.user.username

    try:
        auth_logout(request)
        return JsonResponse({
            "username": username,
            "status": True,
            "message": "Logout succeed!"
        }, status=200)
    except:
        return JsonResponse({
        "status": False,
        "message": "Logout failed."
        }, status=401)
