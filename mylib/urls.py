from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # url(r'^libs/', include('libs.urls', namespace='libs')),
    url(r'^', include('libs.urls', namespace='libs')),
    url(r'^admin/', include(admin.site.urls)),
]
