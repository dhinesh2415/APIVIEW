from django.contrib import admin
from django.urls import path,include
from App1 import views

urlpatterns = [
    path('api/', include('App1.urls')),
    path('admin/', admin.site.urls),
    path('',views.create,name='create'),
    path('update/<int:id>/',views.edit,name='update'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
