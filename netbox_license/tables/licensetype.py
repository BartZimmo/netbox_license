from django.db.models import Sum
from django_tables2 import tables, TemplateColumn
from netbox.tables import NetBoxTable
from django.urls import reverse
from django.utils.html import format_html
from ..models import License, LicenseAssignment, LicenseType
from ..template_content import LICENSE_EXPIRY_PROGRESSBAR_TABLE

# ---------- LicenseType ----------

class LicenseTypeTable(NetBoxTable):
    name = tables.Column(linkify=True)
    slug = tables.Column()
    manufacturer = tables.Column(verbose_name="Manufacturer", linkify=True)

    instances = tables.Column(
        verbose_name="Instances",
        accessor="license_count",
        order_by="license_count",
        empty_values=(),
    )

    def render_instances(self, value, record):
        url = reverse('plugins:netbox_license:license_list') + f'?license_type_id={record.pk}'
        return format_html('<a href="{}">{}</a>', url, value)

    base_license = tables.Column(
        accessor='base_license',
        verbose_name='Base License',
        linkify=True
    )
    product_code = tables.Column(verbose_name="Product Code")
    ean_code = tables.Column(verbose_name="EAN Code")
    volume_type = tables.Column(verbose_name="Volume Type")
    volume_relation = tables.Column(verbose_name="Volume Relation")
    license_model = tables.Column(verbose_name="License Model")
    purchase_model = tables.Column(verbose_name="Purchase Model")
    description = tables.Column()

    class Meta(NetBoxTable.Meta):
        model = LicenseType
        fields = (
            "id", "name", "slug", "manufacturer","base_license",
            "product_code", "ean_code",
            "volume_type", "volume_relation", "license_model", "purchase_model",
            "description"
        )
        default_columns = (
            "name", "manufacturer","base_license",
            "product_code", "volume_type",
            "license_model", "instances",
        )
