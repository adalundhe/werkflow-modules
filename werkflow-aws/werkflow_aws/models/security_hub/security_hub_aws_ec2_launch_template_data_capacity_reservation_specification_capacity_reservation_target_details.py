from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityHubAwsEc2LaunchTemplateDataCapacityReservationSpecificationCapacityReservationTargetDetails(BaseModel):
    CapacityReservationId: StrictStr | None = None
    CapacityReservationResourceGroupArn: StrictStr | None = None
