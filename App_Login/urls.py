from django.urls import path
from App_Login import views


app_name='app_login'
urlpatterns = [
    path('signup/',views.sign_up,name='signup'),
    path('login/',views.login_page,name='login'),
    path('logout/',views.logout_page,name='logout'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
    path('profile/',views.profile,name='profile'),
    path('profile_search/<username>/',views.profile_others,name='profile_other')
]
