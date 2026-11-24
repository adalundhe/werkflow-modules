from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LightsailGetRelationalDatabaseParametersRequest(BaseModel):
    relationalDatabaseName: StrictStr
    pageToken: StrictStr | None = None
