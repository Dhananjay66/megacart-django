from django.contrib import admin
from django.urls import path, include
from . import views 
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('home', views.home, name = 'home'),
    path('store/',include('store.urls')),
    path('accounts/',include('accounts.urls')),
    path('cart/',include('carts.urls')),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])