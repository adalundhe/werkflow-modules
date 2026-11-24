from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_relational_database_event import LightsailRelationalDatabaseEvent


class LightsailGetRelationalDatabaseEventsResponse(BaseModel):
    relationalDatabaseEvents: list[LightsailRelationalDatabaseEvent] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
