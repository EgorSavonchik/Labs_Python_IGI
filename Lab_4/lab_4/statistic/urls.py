from .views import statistic_show
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

app_name = 'statistic'

urlpatterns = [
    path('', statistic_show, name='statistic')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)