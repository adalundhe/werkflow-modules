from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SecurityLakeListDataLakeExceptionsRequest(BaseModel):
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
    regions: list[StrictStr] | None = None
