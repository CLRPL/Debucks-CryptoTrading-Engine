from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'main/index.html'

class DashboardPageView(TemplateView):
    template_name = 'main/dashboard.html'
class SwapPageView(TemplateView):
    template_name = 'main/swap.html'
class ContactUsPageView(TemplateView):
    template_name = 'main/contact.html'
class SettingsPageView(TemplateView):
    template_name = 'main/splash.html'
class ApiPageView(TemplateView):
    template_name = 'main/api.html'


class ChangeLanguageView(TemplateView):
    template_name = 'main/change_language.html'
