from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class SESMultiRegionEndpoint(BaseModel):
    EndpointName: StrictStr | None = None
    Status: StrictStr | None = None
    EndpointId: StrictStr | None = None
    Regions: list[StrictStr] | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    LastUpdatedTimestamp: datetime.datetime | StrictStr | None = None
