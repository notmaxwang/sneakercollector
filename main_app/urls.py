from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('sneakers/', views.sneakers_index, name='index'),
    path('sneakers/<int:sneaker_id>/', views.sneakers_detail, name='detail'),
    path('sneakers/create/', views.SneakerCreate.as_view(), name='sneakers_create'),
    path('sneakers/<int:pk>/update/', views.SneakerUpdate.as_view(), name='sneakers_update'),
    path('sneakers/<int:pk>/delete/', views.SneakerDelete.as_view(), name='sneakers_delete'),
    path('sneakers/<int:sneaker_id>/add_cleaned/', views.add_cleaned, name='add_cleaned'),
    path('sneakers/<int:sneaker_id>/assoc_shoelace/<int:shoelace_id>/', views.assoc_shoelace, name='assoc_shoelace'),
    path('sneakers/<int:sneaker_id>/unassoc_shoelace/<int:shoelace_id>/', views.unassoc_shoelace, name='unassoc_shoelace'),
]