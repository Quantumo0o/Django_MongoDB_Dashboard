import logging

from django.db import models
from django.db.models import Avg, Q, Sum
from django.shortcuts import render
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from myapp.models import Insight
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

from .models import Insight


class InsightFilter(filters.FilterSet):
    published_year = filters.NumberFilter(field_name='published', lookup_expr='year')
    topic = filters.CharFilter(field_name='topic', lookup_expr='iexact')
    sector = filters.CharFilter(field_name='sector', lookup_expr='iexact')
    region = filters.CharFilter(field_name='region', lookup_expr='iexact')

    class Meta:
        model = Insight
        fields = ['topic', 'sector', 'region', 'published_year']



class InsightListAPIView(GenericAPIView):
    queryset = Insight.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = InsightFilter

    def get(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        print(queryset)

##        if not queryset.exists():
##            return Response([])


        # Aggregate data for intensity by country
        aggregated_intensity = queryset.values('country').annotate(
            total_intensity=Sum('intensity')
        )

        # Aggregate data for likelihood and relevance by country
        aggregated_likelihood_relevance = queryset.values('country').annotate(
            total_likelihood=Avg('likelihood'),
            total_relevance=Avg('relevance')
        )

        # Aggregate data for intensity and relevance by topic
        aggregated_topic_relevance = queryset.values('topic').annotate(
            total_intensity=Avg('intensity'),
            total_relevance=Avg('relevance')
        )

        response_data = {
            'aggregated_intensity': list(aggregated_intensity),
            'aggregated_likelihood_relevance': list(aggregated_likelihood_relevance),
            'aggregated_topic_relevance': list(aggregated_topic_relevance)
        }

        return Response(response_data)

def count_null_and_valid(field_name):
    fieldstats = Insight._meta.get_field(field_name)
    null_query = Q(**{field_name: None})

    if isinstance(fieldstats, models.CharField) or isinstance(fieldstats, models.TextField):
        null_query |= Q(**{field_name: ""})

    
    total_count = Insight.objects.all().count()
    null_count = Insight.objects.filter(null_query).count()/total_count*100
    valid_count = (total_count - null_count)/total_count*100

    return {'null_count': round(null_count,2), 'total_count': total_count, 'valid_count': round(valid_count,2)}
    

def dashboard(request):
    regions = Insight.objects.values_list('region', flat=True).exclude(region='').distinct()
    topics = Insight.objects.values_list('topic', flat=True).exclude(topic='').distinct().exclude()
    sectors = Insight.objects.values_list('sector', flat=True).exclude(sector='').distinct()
    sources = Insight.objects.values_list('source', flat=True).exclude(source='').distinct()
    published_date = Insight.objects.values_list('published', flat=True).exclude(region='').distinct()
    published_dates = set([date.year for date in published_date if date is not None])


    field_counts = {}

    field_counts['end_year'] = count_null_and_valid('end_year')
    field_counts['intensity'] = count_null_and_valid('intensity')
    field_counts['sector'] = count_null_and_valid('sector')
    field_counts['topic'] = count_null_and_valid('topic')
    field_counts['insight'] = count_null_and_valid('insight')
    field_counts['url'] = count_null_and_valid('url')
    field_counts['region'] = count_null_and_valid('region')
    field_counts['start_year'] = count_null_and_valid('start_year')
    field_counts['impact'] = count_null_and_valid('impact')
    field_counts['added'] = count_null_and_valid('added')
    field_counts['published'] = count_null_and_valid('published')
    field_counts['country'] = count_null_and_valid('country')
    field_counts['relevance'] = count_null_and_valid('relevance')
    field_counts['pestle'] = count_null_and_valid('pestle')  # Assuming this is a field name
    field_counts['source'] = count_null_and_valid('source')
    field_counts['title'] = count_null_and_valid('title')
    field_counts['likelihood'] = count_null_and_valid('likelihood')

    # Print null and valid counts for each field
    for field, counts in field_counts.items():
        null_count = counts['null_count']
        valid_count = counts['valid_count']
        print(f"Field: {field}")
        print(f"\tNull Count: {null_count}")
        print(f"\tValid Count: {valid_count}")
        print("-" * 20)

    
    context = {
        'regions': regions,
        'topics': topics,
        'sectors': sectors,
        'sources': sources,
        'published_dates': published_dates,
        'field_counts': field_counts,
    }
    return render(request, 'dashboard.html', context)

