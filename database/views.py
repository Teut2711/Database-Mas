from .backend import run
from .forms import NSDLForm
from django.views.generic.edit import FormView
from  django.views.generic.base import TemplateView
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
redirect


class SuccessView(TemplateView):
    template_name = 'database/success.html'

    # make the dictionary available in the template as "stats"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['stats'] = self.request.session['stats']
        return context


class NSDLView(FormView):
    template_name = 'database/nsdl.html'
    form_class = NSDLForm
    success_url = '/success/'

    def form_valid(self, form):
        
        stats = run.main(form.cleaned_data["filepath"])
        print(stats)
        self.request.session['stats'] = stats
        return super().form_valid(form)

    def form_invalid(self, form):
        return HttpResponse("Invalid Form")