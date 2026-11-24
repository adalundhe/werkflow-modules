from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_container_service_log_event import LightsailContainerServiceLogEvent


class LightsailGetContainerLogResponse(BaseModel):
    logEvents: list[LightsailContainerServiceLogEvent] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
