from django.urls import re_path
import users.views as users

app_name = 'users'

urlpatterns = [
    re_path(r'^login/', users.login, name='login'),
    re_path(r'^register/', users.registration, name='registration'),
    re_path(r'^profile/', users.profile, name='profile'),
    re_path(r'^logout/', users.logout, name='logout'),

]