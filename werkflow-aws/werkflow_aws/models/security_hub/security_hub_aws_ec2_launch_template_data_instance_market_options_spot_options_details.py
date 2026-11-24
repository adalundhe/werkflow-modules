from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityHubAwsEc2LaunchTemplateDataInstanceMarketOptionsSpotOptionsDetails(BaseModel):
    BlockDurationMinutes: StrictInt | None = None
    InstanceInterruptionBehavior: StrictStr | None = None
    MaxPrice: StrictStr | None = None
    SpotInstanceType: StrictStr | None = None
    ValidUntil: StrictStr | None = None
