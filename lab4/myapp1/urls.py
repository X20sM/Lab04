from django.urls import path
from . import views
urlpatterns=[
  path("",views.index,name="index"),
  path('<int:number>/', views.calculate_total_price, name='calculate_total_price'),
  path('taxrate/', views.tax_rate_view, name='tax_rate_view'),
]

