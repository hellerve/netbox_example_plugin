from django.contrib.auth.mixins import PermissionRequiredMixin
from django.forms.models import model_to_dict
from django.shortcuts import render, redirect

from dcim.models import Device, Interface
from utilities.views import (
    BulkDeleteView, BulkImportView, ObjectEditView, ObjectListView,
)
from . import filters, forms, tables
from .models import Example


class ExampleListView(ObjectListView):
    queryset = Example.objects.all()
    filter = filters.ExampleFilter
    filter_form = forms.ExampleFilterForm
    table = tables.ExampleTable
    template_name = 'example/example_list.html'


class ExampleCreateView(PermissionRequiredMixin, ObjectEditView):
    permission_required = 'example.add_example'
    model = Example
    model_form = forms.ExampleForm
    default_return_url = 'example:example_list'


class ExampleEditView(ExampleCreateView):
    permission_required = 'example.change_example'


class ExampleBulkImportView(PermissionRequiredMixin, BulkImportView):
    permission_required = 'example.add_example'
    model_form = forms.ExampleCSVForm
    table = tables.ExampleTable
    default_return_url = 'example:example_list'


class ExampleBulkDeleteView(PermissionRequiredMixin, BulkDeleteView):
    permission_required = 'example.delete_example'
    queryset = Example.objects
    filter = filters.ExampleFilter
    table = tables.ExampleTable
    default_return_url = 'example:example_list'
