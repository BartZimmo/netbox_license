from netbox.api.viewsets import NetBoxModelViewSet
from netbox_license.models import License, LicenseAssignment, LicenseType
from .serializers import LicenseTypeSerializer, LicenseSerializer, LicenseAssignmentSerializer
from netbox_license.filtersets import licensetypes, LicenseFilterSet, licenseassignments


class LicenseTypeViewSet(NetBoxModelViewSet):
    """API viewset for managing License Types"""
    queryset = LicenseType.objects.all()
    serializer_class = LicenseTypeSerializer
    filterset_class = licensetypes.LicenseTypeFilterSet

class LicenseViewSet(NetBoxModelViewSet):
    """API view for managing Licenses"""
    queryset = License.objects.all()
    serializer_class = LicenseSerializer
    filterset_class = LicenseFilterSet

class LicenseAssignmentViewSet(NetBoxModelViewSet):
    """API viewset for managing LicenseAssignments"""
    queryset = LicenseAssignment.objects.all()
    serializer_class = LicenseAssignmentSerializer
    filterset_class = licenseassignments.LicenseAssignmentFilterSet

