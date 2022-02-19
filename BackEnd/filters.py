from django import forms
from .models import News
import django_filters
 
 # News過濾器

class NewsFilter(django_filters.FilterSet):
 
    # 模糊查詢 icontains，精準查詢iexact
    title = django_filters.CharFilter(
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    date = django_filters.CharFilter(
        widget=forms.NumberInput(attrs={'class': 'form-control'}))

    class Meta:
        model = News
        fields = ('title', 'date')