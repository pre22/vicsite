from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, PasswordChangeView
from django.urls import reverse_lazy
from django.http import request, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, CreateView, UpdateView

# 3rd Party app
import logging

# Django-app imports 
from accounts.models import Balance, Profilepic, CustomUser
from accounts.forms import CustomLoginForm, CustomSignupForm



# Create your views here.
class CustomLoginView(LoginView):
    form_class = CustomLoginForm
    template_name = "registration/login.html"
    success_url = reverse_lazy("home")

    # DB Logger 
    db_logger = logging.getLogger('db')
    db_logger.info('info message')
    db_logger.warning('warning message')

    try:
        1/0
    except Exception as e:
        db_logger.exception(e)
    ####################


def SignupView(request):
    if request.method == "POST":
        form = CustomSignupForm(request.POST)

        if form.is_valid():
            form.save(request)
            return HttpResponseRedirect(reverse_lazy("login"))
    else:
        form = CustomSignupForm()

    # DB Logger 
    db_logger = logging.getLogger('db')
    db_logger.info('info message')
    db_logger.warning('warning message')

    try:
        1/0
    except Exception as e:
        db_logger.exception(e)
    ####################

    return render(request, "registration/register.html", {"form": form})

class ProfileView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy('login')
    template_name = "accounts/profile.html"

    # DB Logger 
    db_logger = logging.getLogger('db')
    db_logger.info('info message')
    db_logger.warning('warning message')

    try:
        1/0
    except Exception as e:
        db_logger.exception(e)
    ####################

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            "bal": Balance.user,
            "pics": Profilepic.user,
        }
        return context
    
class ProfileEdit(LoginRequiredMixin, UpdateView):
    model = CustomUser
    fields = (
        "firstname",
        "lastname",
        "occupation",
        "email",
        "phone",
        "sex",
    )
    success_url = reverse_lazy("profile")
    template_name = "accounts/profile_edit.html"

    # DB Logger 
    db_logger = logging.getLogger('db')
    db_logger.info('info message')
    db_logger.warning('warning message')

    try:
        1/0
    except Exception as e:
        db_logger.exception(e)
    ####################

class ProfilePicsView(LoginRequiredMixin, UpdateView):
    model = Profilepic
    fields = {"img",}
    template_name = "accounts/profile_edit.html"
    context_object_name = "pics"
    success_url = reverse_lazy("profile")

    # DB Logger 
    db_logger = logging.getLogger('db')
    db_logger.info('info message')
    db_logger.warning('warning message')

    try:
        1/0
    except Exception as e:
        db_logger.exception(e)
    ####################

class CustomPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name = "accounts/change_password.html"
    success_url = reverse_lazy("profile")

    # DB Logger 
    db_logger = logging.getLogger('db')
    db_logger.info('info message')
    db_logger.warning('warning message')

    try:
        1/0
    except Exception as e:
        db_logger.exception(e)
    ####################
    
# def ProfileEdit(request, id):
#     data = get_object_or_404(CustomUser, id=id)
#     form = ProfileUpdateForm(instance=data)

#     if request.method == "POST":
#         message = "Your Profile has been successfully updated!"
#         form = ProfileUpdateForm(request.POST, instance=data)

#         if form.is_valid():
#             form.save(request)
#             messages.success(request, message)
#             return reverse_lazy("profile")
#     else:
#         form = ProfileUpdateForm(instance=data)
#     return render(request, "accounts/profile_edit.html", {"form": form})

# def ProfilePicsView(request, id):
#     data = get_object_or_404(Profilepic, id=id)
#     form = Profilepic(instance=data)

#     if request.method == "POST":
#         form = ProfilePicForm(request.POST, instance=pic)

#         if form.is_valid():
#             form.save(request)
#             return reverse_lazy("profile")
#     else:
#         form = ProfilePicForm(instance=data)
#     return render(request, "accounts/profile_edit.html", {"pics": form})



