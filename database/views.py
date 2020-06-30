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
        ctx = super().get_context_data(**kwargs)
        ctx['stats'] = self.request.session['stats']
        return ctx


class NSDLView(FormView):
    template_name = 'database/nsdl.html'
    form_class = NSDLForm
    success_url = '/success/'

    def form_valid(self, form):
        stats = run.main(form.cleaned_data["filepath"])
        self.request.session['stats'] = stats
        return super().form_valid()

    def form_invalid(self, form):
        return HttpResponse("Invalid Form")
