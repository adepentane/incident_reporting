from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from categories.serializers import CategorySerializer
from django.shortcuts import render
from categories.models import Category
from reports.models import Report
from django.shortcuts import render



class ActiveCategoryList(generics.ListAPIView):
    queryset = Category.objects.filter(is_active=True)
    serializer_class = CategorySerializer


def home(request):
    categories = Category.objects.all()
    latest_reports = Report.objects.filter(is_active=True).order_by('-created_at')[:5]
    return render(request, 'frontend/home.html', {
        'categories': categories,
        'latest_reports': latest_reports,
    })


def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    reports = Report.objects.filter(category=category, is_active=True).order_by('-created_at')
    return render(request, 'frontend/category_detail.html', {'category': category, 'reports': reports})

def about_us(request):
    return render(request, 'frontend/about_us.html')