""" Central e-commerce Urls. """

# Django
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    # Admin    
    path('admin/', admin.site.urls),

    # ecommerce
    path('ecommerce/', include(('ecommerce.urls','ecommerce'),namespace='ecommerce')),
    
    # user
    path('')

]
