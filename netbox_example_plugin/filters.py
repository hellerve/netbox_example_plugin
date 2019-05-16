import django_filters
from django.db.models import Q

from .models import Example

class ExampleFilter(django_filters.FilterSet):
    q = django_filters.CharFilter(
        method='search',
        label='Search',
    )
    example = django_filters.NumberFilter(
        method='filter_example',
        label='Example',
    )

    class Meta:
        model = Example
        fields = ['description', 'example']

    def search(self, queryset, name, value):
        if not value.strip():
            return queryset
        return queryset.filter(description__icontains=value)

    def filter_example(self, queryset, name, value):
        if not value:
            return queryset
        return queryset.filter(example=value)
