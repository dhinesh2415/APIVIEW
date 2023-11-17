from django.urls import path
from .views import StudentList,StudentDetail
 
urlpatterns = [
    # path('', views.ApiOverview, name='home')
    path('Student/', StudentList.as_view(), name='Student-List'),
    path('Student/<int:pk>/', StudentDetail.as_view(), name='Student-detail'),
]