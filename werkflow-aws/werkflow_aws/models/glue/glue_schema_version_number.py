from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt


class GlueSchemaVersionNumber(BaseModel):
    LatestVersion: StrictBool | None = None
    VersionNumber: StrictInt | None = None
