from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .redshift_event import RedshiftEvent


class RedshiftDescribeEventsResponse(BaseModel):
    Marker: StrictStr | None = None
    Events: list[RedshiftEvent] | None = None
    ResponseMetadata: dict[str, Any] | None = None
