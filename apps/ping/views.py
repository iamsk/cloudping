from django.views.generic import TemplateView
from django.db.models import Count
from collections import defaultdict
from .models import Service, Company, Region


class IndexView(TemplateView):
    template_name = "cloudping.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['cs'] = Company.objects.order_by('order').all()
        context['company'] = 'all'
        rs = Service.objects.filter(status=0).values('company').annotate(total=Count('company')).order_by('-total')
        companies, counts = [], []
        for r in rs:
            companies.append(Company.objects.get(pk=r['company']))
            counts.append(r['total'])

        locations = Region.objects.order_by('order')
        location_objs = []
        for location in locations:
            location_obj = [location]
            for c in companies:
                location_obj.append(bool(Service.objects.filter(company=c, region=location)))
            location_objs.append(location_obj)

        context['companies'] = companies
        context['counts'] = counts
        context['locations'] = location_objs
        return context


class CompanyView(TemplateView):
    template_name = "company.html"

    def get_context_data(self, **kwargs):
        context = super(CompanyView, self).get_context_data(**kwargs)
        context['cs'] = Company.objects.order_by('order').all()
        context['company'] = Company.objects.filter(code=kwargs['code']).first()
        context['ss'] = Service.objects.filter(company=context['company'], status=0).order_by('region__order')
        return context
