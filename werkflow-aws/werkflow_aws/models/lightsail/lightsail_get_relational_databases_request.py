from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetRelationalDatabasesRequest(BaseModel):
    pageToken: StrictStr | None = None
