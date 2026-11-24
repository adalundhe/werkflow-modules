from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .lightsail_relational_database_bundle import LightsailRelationalDatabaseBundle


class LightsailGetRelationalDatabaseBundlesResponse(BaseModel):
    bundles: list[LightsailRelationalDatabaseBundle] | None = None
    nextPageToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
