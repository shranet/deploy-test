from django.urls import path
from django.views.generic import TemplateView
from .models import Languages


urlpatterns = [
    path("", TemplateView.as_view(template_name="index.html", extra_context={
        'languages': Languages.objects.order_by('id').all()
    }), name="index"),
    path("about/", TemplateView.as_view(template_name="about.html"), name="about")
]
