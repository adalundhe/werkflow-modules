from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSDeleteMigrationProjectRequest(BaseModel):
    MigrationProjectIdentifier: StrictStr
