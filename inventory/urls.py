from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'get_product_price/(?P<product_id>[0-9]+)/$',views.get_product_price),
    url(r'update_product_price/(?P<product_id>[0-9]+)/$',views.update_product_price),
    url(r'last_month_product_pricing/(?P<product_id>[0-9]+)/$',views.last_month_product_pricing),
]
