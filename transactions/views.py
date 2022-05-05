from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, TemplateView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import request, HttpResponseRedirect, HttpResponse

from accounts.models import Balance
from transactions.models import Deposit, Withdraw
from investments.models import Investment
from transactions.forms import WithdrawForm, DepositForm
from accounts.models import Coin, CoinAddress
from accounts.models import CustomUser


# class DepositView(CreateView):
#     """
#     This class handles the deposit request form
#     """

#     model = Deposit
#     form_class = DepositForm
#     template_name = "transactions/deposit.html"

@login_required(login_url="/accounts/login")
def DepositView(request):
    if request.method == "POST":
        form = DepositForm(request.POST)

        if form.is_valid():
            form.save(request)
            return HttpResponse("It is saved")
    else:
        form = DepositForm()
    return render(request, "transactions/deposit.html", {"form": form})

class TransactionHistoryView(LoginRequiredMixin, TemplateView):
    """
    This class displays the Transaction history for a user
    """
    login_url = reverse_lazy("login")
    # model = Investment
    template_name = "transactions/transactions.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context = {
            "withdraw_h": Withdraw.objects.filter(user=self.request.user),
            "deposit_h": Deposit.objects.filter(user=self.request.user),
            "invest_h": Investment.objects.filter(user=self.request.user) 
        }
        return context
    

# class WithdrawView(CreateView):
#     """
#     This class handles the form for withdraw request
#     """

#     model = Withdraw
#     form_class = WithdrawForm
#     template_name = "transactions/withdrawal.html"
#     success_url = reverse_lazy("home")
    
    # extra_context = {
    #     "coin": Coin.objects.all(),
    #     "coin_ad": CoinAddress.objects.all(),
    # }

@login_required(login_url="/accounts/login")
def WithdrawView(request):
    if request.method == "POST":
        form = WithdrawForm(request.POST)
        if form.is_valid():
            form.save(request)
            return HttpResponse("Submitted")
    else:
        form = WithdrawForm()
    return render(request, "transactions/withdrawal.html", {"form": form})
        




