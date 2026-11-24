from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailRebootRelationalDatabaseRequest(BaseModel):
    relationalDatabaseName: StrictStr
