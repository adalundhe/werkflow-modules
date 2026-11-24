from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSDeleteDataMigrationRequest(BaseModel):
    DataMigrationIdentifier: StrictStr
