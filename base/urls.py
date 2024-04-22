from django.urls import path
from .views import TaskList,TaskDetail,TaskCreate,TaskUpdate,TaskDelete,LoginPage,RegisterPage
from django.contrib.auth.views import LogoutView



urlpatterns=[
    path('login/',LoginPage.as_view(),name="login"),
    path('logout/',LogoutView.as_view(next_page="login"),name="logout"),
    path('register/',RegisterPage.as_view(),name='register'),
    path('',TaskList.as_view(),name="taskList"),
    path('task/<int:pk>/',TaskDetail.as_view(),name="taskDetail"),
    path('create-task/',TaskCreate.as_view(),name="taskCreate"),
    path('update-task/<int:pk>/',TaskUpdate.as_view(),name="taskUpdate"),
    path('delete-task/<int:pk>/',TaskDelete.as_view(),name="taskDelete"),
]