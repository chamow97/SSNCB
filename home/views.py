from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response
from django.views import View
from TwitterAPI import TwitterAPI
from home.forms import UserForm

def index(request):
    return render(request, 'home/index.html')

class UserFormView(View):
    form_class = UserForm
    template_name = 'home/registration_form.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'home/index.html')

        return render(request, 'home/'+self.template_name, {'form':form})

def login_user(request):
    if not request.user.is_authenticated():
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'home/index.html')
                else:
                    return render(request, 'home/login_user.html',
                                  {'error_message' : 'Your account has been disabled!'})
            else:
                return render(request, 'home/login_user.html',
                              {'error_message': 'Incorrect Username / Password!'})

    return render(request, 'home/login_user.html')

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        'form': form
    }
    return render(request, 'home/login_user.html')

def construction(request):
    return render(request, 'home/construction.html')

