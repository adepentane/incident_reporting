from rest_framework import viewsets
from .models import Category
from .serializers import CategorySerializer
from rest_framework.permissions import IsAdminUser
from django.shortcuts import render, get_object_or_404
from .models import Category
from reports.models import Report  # Import Report model


def category_list(request):
    categories = Category.objects.filter(is_active=True)
    return render(request, 'categories/category_list.html', {'categories': categories})

def category_detail(request, pk):
    category = get_object_or_404(Category, pk=pk)
    reports = Report.objects.filter(category=category).order_by('-created_at')  # Order reports by creation date in descending order
    return render(request, 'categories/category_detail.html', {'category': category, 'reports': reports})


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
