from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class Route53DomainsViewBillingRequest(BaseModel):
    Start: datetime.datetime | StrictStr | None = None
    End: datetime.datetime | StrictStr | None = None
    Marker: StrictStr | None = None
    MaxItems: StrictInt | None = None
