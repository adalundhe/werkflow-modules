from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListPackagesRequest(BaseModel):
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
