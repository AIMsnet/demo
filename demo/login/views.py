from django.shortcuts import render, HttpResponseRedirect, redirect
from django.contrib.auth import views as auth_views
from django.contrib.auth import login, authenticate
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

class userLogin(auth_views.LoginView):    
    def form_valid(self, form):
        login(self.request, form.get_user())
        print('userlogin')
        self.request.session['username'] = self.request.user.username
        print(self.request.session['username'])
        # return HttpResponseRedirect(self.get_success_url())
        return HttpResponseRedirect("/login/welcomPage/")

def signup(request):
    form = UserCreationForm(request.POST)
    print("in")
    if form.is_valid():
        form.save()
        print("user created")
        # username = form.cleaned_data.get('username')
        # password = form.cleaned_data.get('password1')
        # user = authenticate(username=username, password=password)
        # login(request, user)
        messages.SUCCESS("User Created Successfully, You Can Login Now. ")
        return redirect('/login/')
    return render(request, 'signup.html', {'form': form})


def logout(request):
    print('logging out')
    request.session.flush()
    print("Session flushed")
    auth.logout(request)
    return redirect("/login/")

def welcomePage(request):
    if request.session.has_key('username'):
        return render(request, "welcome.html")
    return redirect("/login/")