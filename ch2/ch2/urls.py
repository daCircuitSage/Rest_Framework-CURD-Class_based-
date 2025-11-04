from django.contrib import admin
from django.urls import path
from app2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('studata/', views.Student_data.as_view()),
    path('studata/<int:pk>', views.Student_data.as_view())
]
