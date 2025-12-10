from datetime import timedelta
from django.utils.timezone import now
from extras.scripts import Script, IntegerVar
from netbox_license.models.license import License

class CheckLicenseSupportStatus(Script):
    """
    Automatically sets the `support_status` field based on days until license expiry:
    - 'expired' if expired
    - 'critical' if expiring within `critical_days`
    - 'warning' if expiring within `warning_days`
    - 'good' if later than that
    """

    class Meta:
        name = "Check License Support Status"
        description = (
            "Automatically updates the `support_status` field to one of: "
            "'expired', 'critical', 'warning', or 'good' based on expiry_date."
        )

    critical_days = IntegerVar(
        description="Days before expiry to trigger 'critical' support status",
        default=30,
        min_value=1,
    )

    warning_days = IntegerVar(
        description="Days before expiry to trigger 'warning' support status (must be greater than critical)",
        default=90,
        min_value=31,
    )

    def run(self, data, commit):
        today = now().date()
        updated = 0

        for lic in License.objects.all():
            expiry_date = lic.expiry_date

            if not expiry_date:
                self.log_debug(lic, "No expiry_date set; skipping")
                continue

            days_until_expiry = (expiry_date - today).days

            # Determine new status
            if days_until_expiry < 0:
                new_status = "expired"
            elif days_until_expiry <= data["critical_days"]:
                new_status = "critical"
            elif days_until_expiry <= data["warning_days"]:
                new_status = "warning"
            else:
                new_status = "good"

            if lic.support_status != new_status:
                old_status = lic.support_status
                lic.support_status = new_status
                if commit:
                    lic.save()
                self.log_success(lic, f"Support status updated: {old_status} → {new_status}")
                updated += 1
            else:
                self.log_debug(lic, f"Support status already '{lic.support_status}', no update")

        self.log_info(None, f"{updated} license(s) updated.")