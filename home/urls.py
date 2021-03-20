from django.urls import path

from . import views

urlpatterns = [
    path('', views.Inventory.as_view(), name= 'home'),
    path('<str:id>/update', views.InventoryUpdate.as_view(), name= 'inventoryUpdate'),
    path('<str:id>/remove', views.InventoryRemove.as_view(), name= 'inventoryRemove')
]
