from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .pinpoint_applications_response import PinpointApplicationsResponse


class PinpointGetAppsResponse(BaseModel):
    ApplicationsResponse: PinpointApplicationsResponse | None = None
    ResponseMetadata: dict[str, Any] | None = None
