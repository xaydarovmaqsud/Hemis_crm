from django.urls import path
from .views import *
urlpatterns=[
    path('guruh/',guruh,name='guruh'),
    path('fan/',fanlar,name='fan'),
    path('talaba/new/',TalabaCreate.as_view(),name='talaba_new'),
    path('talaba/<int:pk>/edit/',TalabaUpdate.as_view(),name='talaba_edit'),
    path('talaba/<int:pk>/delete/',TalabaDelete.as_view(),name='talaba_delete'),
    path('guruh/new/',GuruhCreate.as_view(),name='guruh_new'),
    path('guruh/<int:pk>/edit/',GuruhUpdate.as_view(),name='guruh_edit'),
    path('guruh/<int:pk>/delete/',GuruhDelete.as_view(),name='guruh_delete'),
    path('mavzu/new/',MavzuCreate.as_view(),name='mavzu_new'),
    path('mavzu/<int:pk>/edit/',MavzuUpdate.as_view(),name='mavzu_edit'),
    path('mavzu/<int:pk>/delete/',MavzuDelete.as_view(),name='mavzu_delete'),
    path('guruh/<int:id>/', byguruh, name='byguruh'),
    path('fan/<int:id>/', byfan, name='byfan'),
]