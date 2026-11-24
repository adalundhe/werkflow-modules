from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .cloud_trail_event import CloudTrailEvent


class CloudTrailLookupEventsResponse(BaseModel):
    Events: list[CloudTrailEvent] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
