from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_relational_database import LightsailRelationalDatabase


class LightsailGetRelationalDatabasesResponse(BaseModel):
    relationalDatabases: list[LightsailRelationalDatabase] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
