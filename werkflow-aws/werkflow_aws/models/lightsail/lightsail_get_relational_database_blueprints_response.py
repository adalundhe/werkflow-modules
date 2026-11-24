from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_relational_database_blueprint import LightsailRelationalDatabaseBlueprint


class LightsailGetRelationalDatabaseBlueprintsResponse(BaseModel):
    blueprints: list[LightsailRelationalDatabaseBlueprint] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
