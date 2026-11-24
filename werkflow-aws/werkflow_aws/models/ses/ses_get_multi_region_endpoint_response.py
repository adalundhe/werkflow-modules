from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .ses_route import SESRoute


class SESGetMultiRegionEndpointResponse(BaseModel):
    EndpointName: StrictStr | None = None
    EndpointId: StrictStr | None = None
    Routes: list[SESRoute] | None = None
    Status: StrictStr | None = None
    CreatedTimestamp: datetime.datetime | StrictStr | None = None
    LastUpdatedTimestamp: datetime.datetime | StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
