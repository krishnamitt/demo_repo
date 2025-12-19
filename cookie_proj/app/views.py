from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")

        response = redirect('profile')
        response.set_cookie('username', username)  # 👈 COOKIE
        return response

    return render(request, "login.html")


def profile(request):
    username = request.COOKIES.get('username')

    if not username:
        return redirect('login')

    role = "Admin" if username == "murali" else "Employee"

    return render(request, "profile.html", {
        "username": username,
        "role": role
    })

def about(request):
    return render(request, "about.html")


def logout_view(request):
    response = redirect('login')
    response.delete_cookie('username')
    return response
