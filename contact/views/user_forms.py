from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from contact.forms import RegisterForm, RegisterUpdateForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Usuário Registrado ! ')
            return redirect('contact:index')

    context = {
        'form': form,
    }

    return render(request, 'contact/register.html', context)


def login_view(request):
    form = AuthenticationForm(request)

    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            messages.success(request, 'Login Feito com Sucesso ! ')
            return redirect('contact:index')

    context = {
        'form': form,
    }

    return render(request, 'contact/login.html', context)


@login_required(login_url='contact:login')
def logout(request):
    messages.success(request, 'Logout Efetuado ! ')
    auth.logout(request)
    return redirect('contact:login')


@login_required(login_url='contact:login')
def user_update(request):
    form = RegisterUpdateForm(instance=request.user)

    if request.method != 'POST':
        return render(request, 'contact/user_update.html', {'form': form})

    form = RegisterUpdateForm(data=request.POST, instance=request.user)

    if not form.is_valid():
        return render(request, 'contact/user_update.html', {'form': form})

    form.save()
    messages.success(request, 'Dados Alterados com Sucesso ! ')
    return redirect('contact:user_update')
