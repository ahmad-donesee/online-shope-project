"""
URL configuration for conig project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from product.views import product_view
from django.conf import settings
from django.conf.urls import include
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns

urlpatterns =i18n_patterns(
    path("",product_view, name='product_view'),
    path('rosetta/', include('rosetta.urls')),
    path(_('admin/'), admin.site.urls),
    path(_("product/"),include("product.urls",namespace="product")), 
    path(_("cart/"),include("cart.urls",namespace="cart")), 
    path(_("register/"),include("register.urls",namespace="register")), 
    path(_("orders/"),include("orders.urls",namespace="orders")), 
    path(_("coupons/"),include("coupons.urls",namespace="coupons")), 
     path(_("zarinpal/"),include("zarinpal.urls",namespace="zarinpal")), 
)
urlpatterns +=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



