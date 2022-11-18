from django.urls import path
from .views import *

app_name = 'database'

urlpatterns = [
    path('site/', SiteView.as_view({'post' : 'create', 'get' : 'list'}), name='create_new_site'),
    path('site_delete/<int:pk>', SiteView.as_view({'delete' : 'destroy'}), name='delete_site'),

    path('service/', ServiceView.as_view({'post' : 'create'}), name='create_new_service'),
    path('service/<int:pk>', ServiceView.as_view({'patch' : 'partial_update', 'delete' : 'destroy'}), name='edit_service'),
    path('services/<int:site_id>', ServiceView.as_view({'get' : 'list'}), name="get_all_services"),

    path('send_blockchain/', BlockchainView.as_view({'post' : 'create'}), name='create_new_blockchain'),
    path('blockchain/<int:pk>', BlockchainView.as_view({'patch' : 'partial_update'}), name='edit_blockchain'),
    path('blockchainn/<int:site_id>', BlockchainView.as_view({'get' : 'list'}), name='get_url_blockchain'),

    path('login/', LoginView.as_view({'post' : 'create'}), name='create_new_login'),
    path('login/<int:pk>', LoginView.as_view({'patch' : 'partial_update', 'delete': 'destroy'}), name='edit_login'),
    path('admin_login/', LoginView.as_view({'get':'login_admin'}), name='login_as_admin'),
    path('user_login/', LoginView.as_view({'get':'login_user'}), name='login_as_user'),

    path('all_data/<int:site_id>', AllInfoView.as_view({'get' : 'list'}), name='get_all_data')
]