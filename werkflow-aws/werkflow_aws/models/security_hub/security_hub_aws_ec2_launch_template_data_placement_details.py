from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsEc2LaunchTemplateDataPlacementDetails(BaseModel):
    Affinity: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    GroupName: StrictStr | None = None
    HostId: StrictStr | None = None
    HostResourceGroupArn: StrictStr | None = None
    PartitionNumber: StrictInt | None = None
    SpreadDomain: StrictStr | None = None
    Tenancy: StrictStr | None = None
