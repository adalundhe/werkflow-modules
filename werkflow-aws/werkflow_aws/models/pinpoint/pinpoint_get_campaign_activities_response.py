from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_activities_response import PinpointActivitiesResponse


class PinpointGetCampaignActivitiesResponse(BaseModel):
    ActivitiesResponse: PinpointActivitiesResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
