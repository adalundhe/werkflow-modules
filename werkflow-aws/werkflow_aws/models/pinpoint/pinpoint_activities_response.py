from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .pinpoint_activity_response import PinpointActivityResponse


class PinpointActivitiesResponse(BaseModel):
    Item: list[PinpointActivityResponse] | None = None
    NextToken: StrictStr | None = None
