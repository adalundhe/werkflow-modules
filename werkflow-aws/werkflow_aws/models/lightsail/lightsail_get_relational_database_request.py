from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetRelationalDatabaseRequest(BaseModel):
    relationalDatabaseName: StrictStr
