from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from accounts import views


urlpatterns = [

    path('', views.index, name='index'),

    path('about/', views.about, name='about'),

    path('pricing/', views.pricing, name='pricing'),

    path('second/', views.second, name='second'),

    path('book/', views.book, name='book'),

    # path('location/', views.location_view, name='location'),

    path('webhook/paid/', views.paid_webhook, name='paid_webhook'),

    path('admin/', admin.site.urls),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)