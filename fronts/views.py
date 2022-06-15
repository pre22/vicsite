# django core modules import 
from django.views.generic import TemplateView, CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, HttpResponseRedirect

# 3rd party import 
import logging

# Django-app imports 
from accounts.models import Contact
from fronts.forms import ContactForm
from transactions.models import Deposit, Package
from contents.models import Carousel_Home, Carousel_About, Who_we_are, Who_we_are_sub, Top_executive, Top_executive_body, Our_offering, AboutUs, Footer, HowToInvest



class HomePageView(TemplateView):
    template_name = "front/homes.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        WHo_we_are_sub = Who_we_are_sub.objects.all()

        # context["carousel_home"] = Carousel_Home.objects.all()
        context = {
            "package": Package.objects.all(),
            "HTI": HowToInvest.objects.all(),
            "aboutus": AboutUs.objects.all(),
            "our_offering": Our_offering.objects.all(),
            "who_we_are": WHo_we_are_sub,
            "carousel_home": Carousel_Home.objects.all(),
            # "blog": response,
        }
        return context


def AboutPage(request):
    # DB Logger 
    db_logger = logging.getLogger('db')
    db_logger.info('info message')
    db_logger.warning('warning message')

    if request.method == "POST":
        form = ContactForm(request.POST)
        # all_fields = ContactForm.declared_fields.keys()
        # print(all_fields)

        if form.is_valid():
            form.save(request)
            return HttpResponseRedirect(reverse_lazy("homepage"))


    else:
        form = ContactForm()
        # print("form invalid")


    carousel_about = Carousel_About.objects.all()
    
    
    return render(request, "front/about.html", {
        "aboutus": AboutUs.objects.all(),
        "carousel_about": carousel_about,
        "form": form,
    })



