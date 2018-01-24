# -*- coding: utf-8 -*-

from django.views.generic import TemplateView
from django.db.models import Count

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
        context['companies'] = companies
        context['counts'] = counts
        context['rows'] = self.get_rows(companies)
        context['description'] = u'主流云平台地域分布及其延迟'
        return context

    @classmethod
    def get_rows(cls, companies):
        locations = Region.objects.order_by('order')
        rows = []
        for location in locations:
            row = [location]
            for c in companies:
                row.append(bool(Service.objects.filter(company=c, region=location)))
            rows.append(row)
        return rows


class CompanyView(TemplateView):
    template_name = "company.html"

    def get_context_data(self, **kwargs):
        context = super(CompanyView, self).get_context_data(**kwargs)
        context['cs'] = Company.objects.order_by('order').all()
        context['company'] = company = Company.objects.filter(code=kwargs['code']).first()
        context['ss'] = Service.objects.filter(company=context['company'], status=0).order_by('region__order')
        context['description'] = company.description
        return context
