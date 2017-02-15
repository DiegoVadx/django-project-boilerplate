from django.conf.urls import url, include

urlpatterns = [
    url(r'^api/', include('apps.__base.api.urls'))
]
