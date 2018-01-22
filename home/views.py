from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, render_to_response, redirect
from django.views import View
from home.forms import UserForm
from .models import contests
from .models import editor_language
from .models import editor_themes

def index(request):
    return render(request, 'index.html')

class UserFormView(View):
    form_class = UserForm
    template_name = 'registration_form.html'

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
                    return render(request, 'index.html')

        return render(request, self.template_name, {'form':form})

def practice(request):
    contest_list = contests.objects.all()
    return render_to_response('practice.html', {'contest_list': contest_list})


def enter(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            username = request.POST["username"]
            password = request.POST["password"]

            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    return render(request, 'login.html',
                                  {'error_message' : 'Your account has been disabled!'})
            else:
                return render(request, 'login.html',
                              {'error_message': 'Incorrect Username / Password!'})

    return render(request, 'login.html')

def online_editor(request):
    languages = editor_language.objects.all()
    themes = editor_themes.objects.all()
    return render_to_response('online_editor.html', {'languages': languages, 'themes': themes})

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        'form': form
    }
    return redirect('/')

def construction(request):
    return render(request, 'construction.html')

