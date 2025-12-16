from utilities.choices import ChoiceSet
from django.utils.translation import gettext_lazy as _

# ---------- LicenseType ----------

class VolumeTypeChoices(ChoiceSet):
    key = 'LicenseType.volume_type'

    SINGLE = 'single'
    VOLUME = 'volume'
    UNLIMITED = 'unlimited'

    CHOICES = [
        (SINGLE, _('Single')),
        (VOLUME, _('Volume')),
        (UNLIMITED, _('Unlimited')),
    ]

class PurchaseModelChoices(ChoiceSet):
    key = 'LicenseType.purchase_model'

    PERPETUAL = 'perpetual'
    SUBSCRIPTION = 'subscription'

    CHOICES = [
        (PERPETUAL, _('Perpetual')),
        (SUBSCRIPTION, _('Subscription')),
    ]

class LicenseModelChoices(ChoiceSet):
    key = 'LicenseType.license_model'

    BASE = 'base'
    EXPANSION = 'expansion'

    CHOICES = [
        (BASE, _('Base License')),
        (EXPANSION, _('Expansion Pack')),
    ]

class VolumeRelationChoices(ChoiceSet):
    key = 'LicenseType.volume_relation'

    CPU = 'cpu'
    CORES = 'cores'
    USERS = 'users'
    PRINTERS = 'printers'
    SYSTEM = 'system'

    CHOICES = [
        (CPU, _('CPU')),
        (CORES, _('Cores')),
        (USERS, _('Users')),
        (PRINTERS, _('Printers')),
        (SYSTEM, _('System')),  
    ]


# ---------- License ----------

class LicenseStatusChoices(ChoiceSet):
    key = 'License.status'

    ACTIVE = 'active'
    INACTIVE = 'inactive'

    CHOICES = [
        (ACTIVE, _('Active'), 'green'),
        (INACTIVE, _('Inactive'), 'gray'),
    ]

class LicenseSupportStatusChoices(ChoiceSet):
    key = 'License.support_status'

    UNKNOWN = 'unknown'
    GOOD = 'good'
    WARNING = 'warning'
    CRITICAL = 'critical'
    EXPIRED = 'expired'

    CHOICES = [
        (UNKNOWN, _('Unknown'), 'gray'),
        (GOOD, _('Good'), 'green'),
        (WARNING, _('Warning'), 'yellow'),
        (CRITICAL, _('Critical'), 'orange'),
        (EXPIRED, _('Expired'), 'red'),
    ]


# ---------- LicenseAssignment ----------

class AssignmentKindChoices(ChoiceSet):
    DEVICE = 'device'
    VM = 'virtual_machine'

    CHOICES = [
        (DEVICE, 'Device'),
        (VM, 'Virtual Machine'),
    ]


class LicenseAssignmentChoices(ChoiceSet):
    FULLY = 'fully'
    PARTLY = 'partly'
    NOT = 'not'

    CHOICES = [
        (FULLY, 'Fully'),
        (PARTLY, 'Partly'),
        (NOT, 'Not'),
    ]
