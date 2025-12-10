from django.db.models import Sum
from django_tables2 import tables, TemplateColumn
from netbox.tables import NetBoxTable
from django.urls import reverse
from django.utils.html import format_html
from ..models import LicenseAssignment
from ..template_content import LICENSE_EXPIRY_PROGRESSBAR_TABLE

# ---------- Assignments ----------

class LicenseAssignmentTable(NetBoxTable):
    
    license_key = tables.Column(
        accessor="license",
        verbose_name="License Key",
        linkify=True
    )
    license_type = tables.Column(
        accessor='license.license_type',
        verbose_name='License Type',
        linkify=True,
        order_by='license__license_type__name'
    )
    manufacturer = tables.Column(
        accessor="license.license_type.manufacturer",
        verbose_name="License Manufacturer",
        linkify=True
    )

    device = tables.Column(
        accessor="device",
        verbose_name="Device",
        linkify=True
    )
    device_type = tables.Column(
        accessor="device.device_type",
        verbose_name="Device Type",
        linkify=True
    )
    device_manufacturer = tables.Column(
        accessor="device.device_type.manufacturer",
        verbose_name="Device Manufacturer",
        linkify=True
    )
    virtual_machine = tables.Column(
        accessor="virtual_machine",
        verbose_name="Virtual Machine",
        linkify=True
    )
    volume = tables.Column(verbose_name="Volume")

    volume_relation = tables.Column(
        accessor="license.license_type.volume_relation",
        verbose_name="Volume Relation",
        order_by="license__license_type__volume_relation"
    )
    assigned_on = tables.Column(verbose_name="Assigned On")
    description = tables.Column(verbose_name="Description")

    class Meta(NetBoxTable.Meta):
        model = LicenseAssignment
        fields = (
            "license_key", "license_type", "manufacturer",
            "device", "device_type", "device_manufacturer",
            "virtual_machine", "volume", "volume_relation",
            "assigned_on", "description"
        )
        default_columns = (
            "license", "device", "virtual_machine", "volume",
        )
            
