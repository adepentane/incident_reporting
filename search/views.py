from rest_framework import viewsets, permissions
from .models import SearchQuery
from .serializers import SearchQuerySerializer
from django.shortcuts import render
from django.db.models import Q
from reports.models import Report
from django.contrib.auth import get_user_model

class SearchQueryViewSet(viewsets.ModelViewSet):
    queryset = SearchQuery.objects.all().order_by('-timestamp')
    serializer_class = SearchQuerySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


def search_results(request):
    query = request.GET.get('query', '')
    if query:
        user = request.user if request.user.is_authenticated else None
        SearchQuery.objects.create(user=user, query=query)

        reports = Report.objects.filter(
            Q(description__icontains=query) |
            Q(category__name__icontains=query)
        ).distinct()

        User = get_user_model()
        users = User.objects.filter(username__icontains=query).distinct()
    else:
        reports = []
        users = []

    return render(request, 'search/results.html', {'query': query, 'reports': reports, 'users': users})
