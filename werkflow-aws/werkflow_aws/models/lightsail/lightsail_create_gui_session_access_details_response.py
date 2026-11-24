from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .lightsail_session import LightsailSession


class LightsailCreateGUISessionAccessDetailsResponse(BaseModel):
    resourceName: StrictStr | None = None
    status: StrictStr | None = None
    percentageComplete: StrictInt | None = None
    failureReason: StrictStr | None = None
    sessions: list[LightsailSession] | None = None
    ResponseMetadata: dict[str, Any] | None = None
