from django.urls import path
from .views import main_page,detail_page,add_model,create_car_2,update_car,delete_car,register,login_user,logout_user

urlpatterns = [
    path('', main_page, name='main_page'),
    path('detail_page/<int:car_id>', detail_page, name='detail_page'),
    path('create_page/', add_model, name='add_model'),
    path('update_car/<int:car_id>', update_car, name='update_car'),
    path('create_car_2/', create_car_2, name='create_car_2'),
    path('car_delete/<int:car_id>',delete_car , name='delete_car'),
    path('register/',register , name='register'),
    path('login/', login_user, name='login'),
    path('logout/',logout_user, name='logout')
]