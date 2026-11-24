from __future__ import annotations
from pydantic import BaseModel, StrictStr


class OpenSearchGetMigrationRequest(BaseModel):
    migrationId: StrictStr
