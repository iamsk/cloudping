from django.views.generic import TemplateView
from .models import Service, Company


class CompanyView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(CompanyView, self).get_context_data(**kwargs)
        context['cs'] = Company.objects.order_by('order').all()
        context['company'] = Company.objects.filter(code=kwargs['code']).first()
        context['ss'] = Service.objects.filter(company=context['company'], status=0)
        return context
