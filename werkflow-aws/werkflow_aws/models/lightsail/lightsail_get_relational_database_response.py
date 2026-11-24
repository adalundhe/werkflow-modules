from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .lightsail_relational_database import LightsailRelationalDatabase


class LightsailGetRelationalDatabaseResponse(BaseModel):
    relationalDatabase: LightsailRelationalDatabase | None = None
    ResponseMetadata: dict[str, Any] | None = None
