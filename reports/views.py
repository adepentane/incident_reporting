from rest_framework import viewsets, permissions
from .models import Report, Image, Video
from .serializers import ReportSerializer, ImageSerializer, VideoSerializer
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import ReportForm
from django.http import HttpResponseForbidden


class ReportViewSet(viewsets.ModelViewSet):
    queryset = Report.objects.all().order_by('-created_at')
    serializer_class = ReportSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


@login_required
def report_create(request):
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES)
        if form.is_valid():
            report = form.save(commit=False)
            report.user = request.user
            report.save()

            # Handle images
            for img in request.FILES.getlist('images'):
                Image.objects.create(report=report, image=img)

            # Handle videos
            for vid in request.FILES.getlist('videos'):
                Video.objects.create(report=report, video=vid)

            messages.success(request, 'Report created successfully.')
            return redirect('reports:report_list')
    else:
        form = ReportForm()
    return render(request, 'reports/report_form.html', {'form': form})


@login_required
def report_update(request, slug):
    report = get_object_or_404(Report, slug=slug, user=request.user)
    if request.method == 'POST':
        form = ReportForm(request.POST, request.FILES, instance=report)
        if form.is_valid():
            form.save()

            # Handle images
            for img in request.FILES.getlist('images'):
                Image.objects.create(report=report, image=img)

            # Handle videos
            for vid in request.FILES.getlist('videos'):
                Video.objects.create(report=report, video=vid)

            messages.success(request, 'Report updated successfully.')
            return redirect('reports:report_list')
    else:
        form = ReportForm(instance=report)
    return render(request, 'reports/report_form.html', {'form': form})


@login_required
def report_list(request):
    reports = Report.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'reports/report_list.html', {'reports': reports})


@login_required
def report_detail(request, slug):
    report = get_object_or_404(Report, slug=slug, user=request.user)
    return render(request, 'reports/report_detail.html', {'report': report})


@login_required
def report_delete(request, slug):
    report = get_object_or_404(Report, slug=slug, user=request.user)
    if request.method == 'POST':
        report.is_active = False
        report.save()
        messages.success(request, 'Report deleted successfully.')
        return redirect('reports:report_list')
    return render(request, 'reports/report_confirm_delete.html', {'report': report})
