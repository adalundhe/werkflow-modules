from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DMSStopDataMigrationRequest(BaseModel):
    DataMigrationIdentifier: StrictStr
