from django.urls import path
from.import views
urlpatterns = [
    path('',views.base,name='base'),
    path('login/',views.login_view,name='login'),
    path('register/',views.register_view,name='register'),
    path('main/',views.main_page,name='main'),
    path('form/',views.form_page,name='form'),
    path('branches/',views.branches_page,name='branches'),
    path('application/',views.application_page,name='application'),
    path('logout/', views.logout_view, name='logout'),



    ]