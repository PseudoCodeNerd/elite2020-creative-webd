from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, View
from accounts.mixins import AdminRequiredMixin
from jobs.models import Job, JobApplication
# Create your views here.
class AdminHome(AdminRequiredMixin, ListView):
    template_name = "admin_dash/home.html"
    def get_queryset(self):
        return Job.objects.all()
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['num_apps'] = JobApplication.objects.count()
        return ctx

class UpdateStatusView(View):
    def get(self, request):
        app_id = request.GET['app_id']
        updated_stat = request.GET['up_stat']
        try:
            app = JobApplication.objects.get(id=int(app_id))
        except ValueError:  
            return HttpResponse(-1)
        app.status = updated_stat
        app.save()
        return HttpResponse(app.status)
        