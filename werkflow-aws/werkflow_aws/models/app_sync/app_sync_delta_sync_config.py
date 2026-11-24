from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AppSyncDeltaSyncConfig(BaseModel):
    baseTableTTL: StrictInt | None = None
    deltaSyncTableName: StrictStr | None = None
    deltaSyncTableTTL: StrictInt | None = None
