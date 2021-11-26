from django.shortcuts import render, redirect
from .models import PostModel
from .forms import PostCreateForm
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm

from django.contrib.auth.models import auth
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def index_view(request):
    context={}
    posts_queryset=PostModel.objects.all()[::-1]
    context['posts_queryset']=posts_queryset
    return render(request, 'index.html',context)


def post_create_view(request):
    context = {}
    form = PostCreateForm()
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.author = request.user
            forms.save()
            return redirect('home_page')
    context['form'] = form
    return render(request, 'post_create.html', context)

def post_read_view(request, post_id):
    context={}
    post_queryset=PostModel.objects.filter(id=post_id).first()
    context['post_queryset'] = post_queryset
    return render(request, 'post_read.html', context)

def post_update_view(request, post_id):
    context = {}
    update_data = PostModel.objects.filter(id=post_id).first()
    form = PostCreateForm(instance=update_data)
    if request.method == 'POST':
        form = PostCreateForm(request.POST, request.FILES, instance=update_data)
        if form.is_valid():
            forms = form.save(commit=False)
            forms.author = request.user
            forms.save()
            return redirect('home_page')
    context['form'] = form
    return render(request, 'post_create.html', context)

def post_delete_view(request, post_id):
    post_delete = PostModel.objects.filter(id=post_id).first()
    post_delete.delete()
    return redirect('home_page')

from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

'''
class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        try:
            user = UserModel.objects.get(email=username)
        except UserModel.DoesNotExist:
            return None
        else:
            if user.check_password(password):
                return user
        return None
'''
'''
def login_view(request):
    context={}
    email=request.POST.get('email')
    raw_password=request.POST.get('password')
    user=authenticate(email=email,password=raw_password)
    if user:
        login(request,user)
        return redirect('home_page')
    else:
        return render(request, 'login.html', context)
'''

class login_view(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'login.html'
    #success_url = reverse_lazy('home_page')

class register_view(generic.CreateView):
    form_class = RegisterForm  #.fields['is_activated'].initial = False  #.cleaned_data(is_activated=False)   #changed_data.__setattr__(self,'is_activated',False)
    template_name = 'register.html'
    success_url = reverse_lazy('login_page')