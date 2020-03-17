from django.views.generic import TemplateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from stream.models import Podcast, LiveShow

class TestPage(LoginRequiredMixin, TemplateView):
	model = LiveShow
	template_name = "live.html"

	def get_context_data(self, *args, **kwargs):
		context = super(TestPage,self).get_context_data(*args, **kwargs)
		context["LiveShow"] = LiveShow.objects.all()[0]
		return context


class ThanksPage(TemplateView):
	template_name = 'thanks.html'