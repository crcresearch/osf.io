from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),

    ### AUTH ###
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^token/', 'rest_framework_jwt.views.obtain_jwt_token'),

    ### API ###
    url(r'^nodes/', include('api.nodes.urls', namespace='nodes')),
] + static('/static/', document_root=settings.STATIC_ROOT)
