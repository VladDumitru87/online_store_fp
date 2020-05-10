from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin


def user_login(request):
    if request.user.is_authenticated:
        return HttpResponse("You are already logged in :)")

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                return HttpResponseRedirect(reverse('index'))
                # return render(request, 'index.html', {"user": user, "message": "Data updated"})
            else:
                return HttpResponse("Your account is inactive.")
        else:

            return HttpResponse("Invalid login details given. Go back and try again")
    else:
        return render(request, 'login.html', {})


def user_logout(request):
    logout(request)

    return redirect('index')


def user_signup(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


class UserProfile(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'user.html'
    context_object_name = 'user'
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        userid = self.kwargs['pk']
        url = reverse_lazy('user-profile', kwargs={'pk': userid})
        return u'%s?%s' % (url, "success=True")


class UsersDelete(LoginRequiredMixin, DeleteView):
    model = User
    template_name = "user_delete.html"
    success_url = reverse_lazy('index')





