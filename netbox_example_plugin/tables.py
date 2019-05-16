import django_tables2 as tables
from django_tables2.utils import Accessor
from utilities.tables import BaseTable, ToggleColumn

from .models import Example

class ExampleTable(BaseTable):
    pk = ToggleColumn()
    example = tables.LinkColumn('example:example_edit', args=[Accessor('pk')])

    class Meta(BaseTable.Meta):
        model = Example
        fields = ('pk', 'example')
