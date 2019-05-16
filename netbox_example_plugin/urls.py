from __future__ import unicode_literals

from django.conf.urls import url

from . import views

app_name = 'netbox_example_plugin'
urlpatterns = [
    url(r'^example/$', views.ExampleListView.as_view(), name='example_list'),
    url(r'^example/add/$', views.ExampleCreateView.as_view(), name='example_add'),
    url(r'^example/import/$', views.ExampleBulkImportView.as_view(), name='example_import'),
    url(r'^example/delete/$', views.ExampleBulkDeleteView.as_view(), name='example_bulk_delete'),
    url(r'^example/(?P<pk>\d+)/edit/$', views.ExampleEditView.as_view(), name='example_edit'),
]
