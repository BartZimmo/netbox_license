# from netbox.jobs import JobRunner, system_job
# from core.choices import JobIntervalChoices
# from netbox_license.models.license import License

# # This job is currently disabled because it currently updates the status, but does not trigger the required event. Use script instead.

# @system_job(interval=JobIntervalChoices.INTERVAL_MINUTELY)
# class LicenseStatusCheckJob(JobRunner):
#     """
#     Job to verify and update license statuses and runs every minute.
#     """

#     class Meta:
#         name = "License Status Checker"

#     def run(self, *args, **kwargs):
#         self.logger.info("Starting License Status Check job...")

#         try:
#             licenses = License.objects.all()
#             self.logger.info(f"Found {licenses.count()} licenses to check.")
#             updated_count = 0
#             for license in licenses:
#                 new_status = license.compute_status()
#                 if license.status != new_status:
#                     self.logger.debug(
#                         f"License {license.pk}: status changed from {license.status} to {new_status}"
#                     )
#                     license.status = new_status
#                     license.save()
#                     updated_count += 1

#             self.logger.info(f"License Status Check completed. Updated {updated_count} licenses.")

#         except Exception as e:
#             # Log the error and re-raise so NetBox marks the job as failed
#             self.logger.error(f"Error during License Status Check: {repr(e)}")
#             raise

# ###### Info:
# # class JobIntervalChoices(ChoiceSet):
# #     INTERVAL_MINUTELY = 1
# #     INTERVAL_HOURLY = 60
# #     INTERVAL_DAILY = 60 * 24
# #     INTERVAL_WEEKLY = 60 * 24 * 7
# #     CHOICES = (
# #         (INTERVAL_MINUTELY, _('Minutely')),
# #         (INTERVAL_HOURLY, _('Hourly')),
# #         (INTERVAL_HOURLY * 12, _('12 hours')),
# #         (INTERVAL_DAILY, _('Daily')),
# #         (INTERVAL_WEEKLY, _('Weekly')),
# #         (INTERVAL_DAILY * 30, _('30 days')),
# #     )
