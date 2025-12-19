from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")

        # storing the username in session
        request.session['username'] = username

        return redirect('profile')

    return render(request, "login.html")


def profile(request):
    # check session
    username = request.session.get('username')

    if not username:
        return redirect('login')

    # owner vs employee logic
    if username.lower() == "murali":
        role = "Owner"
    else:
        role = "Employee"

    return render(request, "profile.html", {
        "username": username,
        "role": role
    })


def about(request):
    return render(request, "about.html")


def logout_view(request):
    request.session.flush()
    return redirect('login')
