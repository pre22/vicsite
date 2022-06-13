from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from investments.models import Investment, Package
from accounts.models import CustomUser

# 3rd party package import 
import logging

class InvestView(LoginRequiredMixin, CreateView):
    """
    This class displays the investment form
    """
    login_url = reverse_lazy("login")
    model = Investment
    template_name = "investments/invest.html"
    fields = ["package", "amount",]
    success_url = reverse_lazy("transactions")
    # context_object_name = "form"

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
        context["user"] = self.request.user
        context["package"] = Package.objects.all()
        
        return context
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
