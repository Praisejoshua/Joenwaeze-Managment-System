from django.urls import path
from .views import SystemListView, ManagementUpdateView, ManagementDeleteView, ManagementForm

urlpatterns = [
    path('', SystemListView.as_view(), name='managment_list'),
    path('update/<int:pk>/', ManagementUpdateView.as_view(), name='managment_update'),
    path('delete/<int:pk>/', ManagementDeleteView.as_view(), name='managment_delete'),
]
