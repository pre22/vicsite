import os
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from django.urls import reverse_lazy
from django.http import request
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import TemplateView, FormView
from django.http import request
from accounts.models import Balance, DueDate, AmountInvested, CustomUser, Profilepic
from transactions.models import Deposit, Package
from contents.models import Carousel_Home, Carousel_About, Who_we_are, Who_we_are_sub, Top_executive, Top_executive_body, Our_offering, AboutUs, Footer, HowToInvest
from site_server.forms import PasswordForm
from mailjet_rest import Client
from decouple import config as cgf



class ChartView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy("login")
    template_name = "charts.html"

    

class DashboardHomeView(LoginRequiredMixin, TemplateView):
    login_url = reverse_lazy("login")
    template_name = "home/home.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            "wallet_bal": Balance.objects.filter(user=self.request.user).first(),
            "amount_invested": AmountInvested.objects.filter(user=self.request.user).first(),
            "duedate": DueDate.objects.filter(user=self.request.user).first(),
            "deposit_h": Deposit.objects.filter(user=self.request.user),
            "pics": Profilepic.objects.filter(user=self.request.user)
        }
        return context
    
 
# class Custom_PasswordResetView(PasswordResetView):
#     template_name = "password/forgot_password.html"
#     subject_template_name = 'password/password_reset_subject.html'
#     email_template_name = 'password/password_reset_email.html'
#     success_url = reverse_lazy("c_password_reset_done")

#     API_KEY = cgf('API_KEY')
#     API_SECRET = cgf('API_SECRET')

#     mailjet = Client(auth=(API_KEY, API_SECRET))
#     data = {
#     'Messages': [
#         {
#         "From": {
#             "Email": "$SENDER_EMAIL",
#             "Name": "Me"
#         },
#         "To": [
#             {
#             "Email": "$RECIPIENT_EMAIL",
#             "Name": "You"
#             }
#         ],
#         "Subject": subject_template_name,
        
#         "HTMLPart": email_template_name
#         }
#     ]
#     }
#     result = mailjet.send.create(data=data)

    
def Custom_PasswordResetView(request):
    MAILJET_API_KEY = cgf('MAILJET_API_KEY')
    MAILJET_API_SECRET = cgf('MAILJET_API_SECRET')
    subject_template_name = 'password/password_reset_subject.html'
    email_template_name = 'password/password_reset_email.html'

    if request.method == 'POST':
        form = PasswordForm(request.POST)

        if form.is_valid():

            subject = subject_template_name
            message = email_template_name
            to_mail = form.cleaned_data['usermail']

            mailjet = Client(auth=(MAILJET_API_KEY, MAILJET_API_SECRET), version='3.1')
            data = {
            'Messages': [
                {
                "From": {
                    "Email": "admin@avaloqsassets.com",
                    "Name": "Me"
                },
                "To": [
                    {

                        "Email": to_mail,
                        # "Name": "You"
                    }
                ],
                "Subject": "<html><title>Avaloqs Password Reset</title></html>",
                
                "HTMLPart": """
                <html>
                <p>You're receiving this email because you requested a password reset for your user account: {{ to_mail }} at avaloqsassets.com, click the link below:
                https://avaloqsassets.com{% url 'c_password_reset_confirm' uidb64=uid token=token %}
                
                If clicking the link above doesn't work, please copy and paste the URL in a new browser window instead/
                
                Thank You for using our site
                
                AvaloqsAssets Team</p>
                </html>
                """
                }
            ]
            }
            result = mailjet.send.create(data=data)
            # print(result.status_code)
            # print(response)
            # response = result.json()
            # return HttpResponseRedirect(reverse_lazy("c_password_reset_done"))
            return redirect("/password_reset/done/")
    else:
        form = PasswordForm()
        
    return render(request, "password/forgot_password.html", {'form': form})


class Custom_PasswordResetDoneView(PasswordResetDoneView):
    template_name = "password/password_reset_done.html"
    success_url = reverse_lazy("c_password_reset_confirm")

class Custom_PasswordResetConfirmView(PasswordResetConfirmView):
    template_name = "password/password_reset_confirm.html"
    success_url = reverse_lazy("c_password_reset_complete")

class Custom_PasswordResetCompleteView(PasswordResetCompleteView):
    template_name = "password/password_reset_complete.html"