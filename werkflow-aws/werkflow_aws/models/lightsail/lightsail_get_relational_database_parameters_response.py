from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_relational_database_parameter import LightsailRelationalDatabaseParameter


class LightsailGetRelationalDatabaseParametersResponse(BaseModel):
    parameters: list[LightsailRelationalDatabaseParameter] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
