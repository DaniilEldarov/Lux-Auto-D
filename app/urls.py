from django.urls import path
from .views import main_page,detail_page

urlpatterns = [
    path('', main_page, name='main_page'),
    path('detail_page/<int:car_id>', detail_page, name='detail_page')
]