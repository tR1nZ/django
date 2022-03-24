from django.urls import re_path
import admins.views as admins

app_name = 'admins'

urlpatterns = [
    re_path(r'^$', admins.index, name='index'),
    re_path(r'^users/$', admins.UserAdminListView.as_view(), name='admin_users'),
    re_path(r'^users-create/$', admins.UserAdminCreateView.as_view(), name='admin_users_create'),
    re_path(r'^users-update/<int:pk>/$', admins.UserAdminUpdateView.as_view(), name='admin_users_update'),
    re_path(r'^users-delete/<int:pk>/$', admins.UserAdminDeleteView.as_view(), name='admin_users_delete'),
]