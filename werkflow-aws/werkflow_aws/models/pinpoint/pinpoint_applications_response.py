from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_application_response import PinpointApplicationResponse


class PinpointApplicationsResponse(BaseModel):
    Item: list[PinpointApplicationResponse] | None = None
    NextToken: StrictStr | None = None
