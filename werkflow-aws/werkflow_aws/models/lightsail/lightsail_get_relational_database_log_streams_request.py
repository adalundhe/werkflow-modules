from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetRelationalDatabaseLogStreamsRequest(BaseModel):
    relationalDatabaseName: StrictStr
