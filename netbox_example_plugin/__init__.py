from netbox.plugins import registry, Plugin

class ExamplePlugin(Plugin):
    """
    The only function a plugin really **needs** to implement is `namespace`.
    """
    def namespace(self):
        """
        this will be the URL namespace that your URLs will find themselves
        inside of
        """
        return 'example'

    def urls(self):
        """
        These are the URLs that you export. We advise you to load them lazily,
        since Django might not be ready yet when this module gets loaded.
        """
        from netbox_example_plugin import urls
        return urls.urlpatterns

    def navbar_elements(self):
        """
        This is arbitrary HTML that will be inlined into the navigation bar.
        """
        return ['example/navbar.html']

    def widgets(self):
        """
        This is arbitrary HTML that will be inlined into the list of widgets.
        """
        return ['example/widget.html']

registry.register(ExamplePlugin())
