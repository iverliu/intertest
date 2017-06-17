from django.conf.urls import url
from sign import viewif

urlpatterns = [
    # guest system interface:
    # ex : /api/add_event/
    url(r'^add_event/', viewif.add_event, name='add_event'),
    # ex : /api/add_guest/
    url(r'^add_guest/', viewif.add_guest, name='add_guest'),
    # ex : /api/get_event_list/
    url(r'^get_event_list/', viewif.get_event_list, name='get_event_list'),
    # ex : /api/get_guest_list/
    url(r'^get_guest_list/', viewif.get_guest_list, name='get_guest_list'),
    #  ex : /api/user_sign/
    url(r'^user_sign/', viewif.user_sign, name='user_sign'),
]