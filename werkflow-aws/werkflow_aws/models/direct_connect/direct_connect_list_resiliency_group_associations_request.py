from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class DirectConnectListResiliencyGroupAssociationsRequest(BaseModel):
    resiliencyGroupId: StrictStr
    maxResults: StrictInt | None = None
    nextToken: StrictStr | None = None
