from netbox.tables import NetBoxTable
import django_tables2 as tables
from django.db.models import Sum
from .models import License, LicenseAssignment


class LicenseTable(NetBoxTable):
    """Table displaying Licenses with clickable links and accurate volume usage."""

    license_key = tables.LinkColumn(
        "plugins:license_management:license_detail",
        args=[tables.A('pk')],
        verbose_name="License Key"
    )
    product_key = tables.Column(verbose_name="Product Key")
    assigned_count = tables.Column(empty_values=(), verbose_name="Assigned Count")

    def render_assigned_count(self, record):
        assigned = record.assignments.aggregate(total=Sum('volume'))['total'] or 0
        if record.assignment_type == "UNLIMITED":
            return f"{assigned}/∞"
        return f"{assigned}/{record.volume_limit}"

    class Meta(NetBoxTable.Meta):
        model = License
        fields = (
            "license_key",
            "product_key",
            "software_name",
            "manufacturer",
            "description",
            "assigned_count",
            "assignment_type",
            "expiry_date",
            "purchase_date",
        )
        default_columns = fields


class LicenseAssignmentTable(NetBoxTable):
    """Table displaying License Assignments clearly and concisely."""

    license = tables.LinkColumn(
        "plugins:license_management:assignment_detail",
        args=[tables.A("pk")],
        verbose_name="License"
    )
    device = tables.Column(verbose_name="Device")
    volume = tables.Column(verbose_name="Volume")
    assigned_to = tables.DateColumn(verbose_name="Assigned On")
    description = tables.Column(verbose_name="Description", empty_values=())

    class Meta(NetBoxTable.Meta):
        model = LicenseAssignment
        fields = ("license", "device", "volume", "assigned_to", "description")
        default_columns = fields
