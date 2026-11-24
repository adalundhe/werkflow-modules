from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class MacieListResourceProfileDetectionsRequest(BaseModel):
    resourceArn: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
