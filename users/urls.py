from django.urls import path
from .views import UserRegistration, UserList, UserDetail, UserDelete, UserDeleteAll


urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user-register'),
    path('user/<int:user_id>/', UserDetail.as_view(), name='user-detail'),
    path('users/', UserList.as_view(), name='user-list'),
    path('delete/<int:user_id>/', UserDelete.as_view(), name='user-delete'),
    path('delete-all/', UserDeleteAll.as_view(), name='user-delete-all')
]
