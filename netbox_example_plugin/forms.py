from django import forms

from .models import Example

from utilities.forms import BootstrapMixin


class ExampleForm(BootstrapMixin, forms.ModelForm):
    class Meta:
        model = Example
        fields = ['example', 'description']
        labels = {
            'example': 'Example Number, useless',
            'description': 'Example Description',
        }


class ExampleCSVForm(forms.ModelForm):
    class Meta:
        model = Example
        fields = Example.csv_headers
        help_texts = {
            'example': 'Example Number, useless',
            'description': 'Neighbor Description',
        }


class ExampleFilterForm(BootstrapMixin, forms.Form):
    model = Example
    q = forms.CharField(
        required=False,
        label='Search'
    )
    example = forms.IntegerField(
        label='example',
        required=False,
    )
