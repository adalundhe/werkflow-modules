from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GlueGetConnectionsFilter(BaseModel):
    MatchCriteria: list[StrictStr] | None = None
    ConnectionType: StrictStr | None = None
    ConnectionSchemaVersion: StrictInt | None = None
