from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
# from django.urls import reverse, reverse_lazy
# from django.views.generic import UpdateView, DeleteView
# from django.contrib.auth.models import User
# from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserSignUpForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# def user_login(request):
#     if request.user.is_authenticated:
#         return redirect('index')
#
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(username=username, password=password)
#         if user:
#             if user.is_active:
#                 login(request, user)
#                 if 'next' in request.POST:
#                     return redirect(request.POST.get('next'))
#                 return HttpResponseRedirect(reverse('index'))
#             else:
#                 return HttpResponse("Your account is inactive.")
#         else:
#
#             return HttpResponse("Invalid login details given. Go back and try again")
#     else:
#         return render(request, 'login.html', {})


# def logout(request):
#     logout(request)
#     return redirect('index')


def home(request):
    return render(request, 'accounts/index.html')


def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:index')

    if request.method == 'POST':
        form = UserSignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            messages.success(request, f'Account created for {username}')
            login(request, user)
            return redirect('accounts:index')
    else:
        form = UserSignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})


# the decorator: To access the profile page, users should login
@login_required
def user(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('user')

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': user_form,
        'p_form': profile_form
    }

    return render(request, 'accounts/user.html', context)








