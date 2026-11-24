from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class IoTListPrincipalThingsRequest(BaseModel):
    principal: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
