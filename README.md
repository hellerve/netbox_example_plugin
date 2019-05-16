# netbox\_example\_plugin

This is an example plugin for the plugin system proposed for Netbox.

## Layout

The plugin registry happens in the module’s `__init__.py`, to assure that it is
run on module import. It’s the entry point into the module.

The rest of the plugin is just a silly Django app that adds a single model to
the core of Netbox, a [widget](), and a [navigation bar extension]().

## Installation

You should be able to add it into Netbox by adding the following line to
Netbox’s `requirement.txt` file and installing the requirements:

```
-e git+http://github.com/hellerve/netbox-example-plugin.git#egg=netbox-example-plugin
```

Then you can enable it by adding the following line to your `configuration.py`:

```python
INSTALLED_APPS = [
    'netbox_example_plugin',
]
```

<hr/>

Have fun!
