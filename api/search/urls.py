from django.conf.urls import url

from api.search import views

app_name = 'osf'

urlpatterns = [
    url(r'^$', views.Search.as_view(), name=views.Search.view_name),
    url(r'^components/$', views.SearchComponents.as_view(), name=views.SearchComponents.view_name),
    url(r'^files/$', views.SearchFiles.as_view(), name=views.SearchFiles.view_name),
    url(r'^projects/$', views.SearchProjects.as_view(), name=views.SearchProjects.view_name),
    url(r'^registrations/$', views.SearchRegistrations.as_view(), name=views.SearchRegistrations.view_name),
    url(r'^users/$', views.SearchUsers.as_view(), name=views.SearchUsers.view_name),
    #url(r'^institutions/$', views.SearchInstitutions.as_view(), name=views.SearchInstitutions.view_name),
    url(r'^ipcores/$', views.SearchIPCores.as_view(), name='SearchIPCores'),
    url(r'^flows/$', views.SearchIPCores.as_view(doc_type='flow'), name='SearchFlows'),
    url(r'^list/$', views.SearchIPCores.as_view(doc_type='ipcore,flow'), name='SearchCoresFlows'),
    # not currently supported by v1, but should be supported by v2
    # url(r'^nodes/$', views.SearchProjects.as_view(), name=views.SearchProjects.view_name),
]
