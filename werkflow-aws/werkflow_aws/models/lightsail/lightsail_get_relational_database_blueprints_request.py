from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetRelationalDatabaseBlueprintsRequest(BaseModel):
    pageToken: StrictStr | None = None
