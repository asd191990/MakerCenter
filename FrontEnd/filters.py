from django import forms
from BackEnd.models import Space
import django_filters
 
 # Space過濾器

class SpaceFilter(django_filters.FilterSet):
 
    # 模糊查詢 icontains，精準查詢iexact
    code = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    name = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Space
        fields = ('code','name')