from django.views.generic import TemplateView


class home(TemplateView):
	template_name = 'index.html'

class about(TemplateView):
	template_name = 'about.html'

class contact(TemplateView):
	template_name = 'contact.html'
