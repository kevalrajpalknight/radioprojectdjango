from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from stream.models import Podcast
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Home(ListView):
    template_name = 'index.html'
    model = Podcast
    paginate_by = 5

class About(TemplateView):
	template_name = 'about.html'


class List_Podcast(LoginRequiredMixin,ListView):
    template_name = "list_podcast.html"
    model = Podcast
    paginate_by = 5

class Detail(LoginRequiredMixin, DetailView):
    model = Podcast
    template_name = "podcast_detail.html"
    