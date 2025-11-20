from netbox.plugins import PluginConfig
from django.urls import include, path
from .version import __version__
from .template_content import template_extensions

class NetboxLicenseConfig(PluginConfig):
    name = 'netbox_license'
    verbose_name = 'NetBox License'
    version = __version__
    description = 'License management Plugin for NetBox'
    base_url = 'license'
    author = 'Bart Van der Biest'
    author_email = 'bart@zimmo.be'
    min_version = '4.4.0'
    default_settings = {
        'top_level_menu': True,
    }

    def ready(self):
        super().ready()
        from . import events
        from . import signals
        from . import jobs

config = NetboxLicenseConfig