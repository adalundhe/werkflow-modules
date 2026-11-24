from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class EC2LaunchTemplateSpotMarketOptions(BaseModel):
    MaxPrice: StrictStr | None = None
    SpotInstanceType: StrictStr | None = None
    BlockDurationMinutes: StrictInt | None = None
    ValidUntil: datetime.datetime | StrictStr | None = None
    InstanceInterruptionBehavior: StrictStr | None = None
