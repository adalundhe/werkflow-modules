from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2SpotPrice(BaseModel):
    AvailabilityZone: StrictStr | None = None
    AvailabilityZoneId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    ProductDescription: StrictStr | None = None
    SpotPrice: StrictStr | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
