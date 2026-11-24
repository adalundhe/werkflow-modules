from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AthenaListEngineVersionsRequest(BaseModel):
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
