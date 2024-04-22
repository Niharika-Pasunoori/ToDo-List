from django.urls import path
from .import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns=[
    path('',views.getRoutes),
    path('tasks/',views.getTasks),
    path('tasks/<int:pk>/',views.getTask),
    path('task-add/',views.addTask),
    path('task-update/<int:pk>/',views.updateTask),
    path('task-delete/<int:pk>/',views.deleteTask),

    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]