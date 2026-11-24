from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class EC2IpamRouteOverlap(BaseModel):
    Prefix: StrictStr | None = None
    Asn: StrictStr | None = None
    DetectedAt: datetime.datetime | StrictStr | None = None
