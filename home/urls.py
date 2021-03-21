from django.urls import path

from . import views

urlpatterns = [
    path('', views.Inventory.as_view(), name= 'home'),
    path('search/<gref>', views.InventorySearch.as_view(), name= 'inventorySearch'),
    path('<str:id>/update', views.InventoryUpdate.as_view(), name= 'inventoryUpdate'),
    path('<str:id>/remove', views.InventoryRemove.as_view(), name= 'inventoryRemove'),
    path('<str:gid>/add', views.InventoryAdd.as_view(), name= 'inventoryAdd'),
]
