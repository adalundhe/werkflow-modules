from __future__ import annotations
from pydantic import BaseModel, StrictStr


class JQLPersonalDataMigrationRequest(BaseModel):
    queryStrings: list[StrictStr] | None = None
