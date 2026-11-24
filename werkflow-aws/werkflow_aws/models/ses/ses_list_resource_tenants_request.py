from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SESListResourceTenantsRequest(BaseModel):
    ResourceArn: StrictStr
    PageSize: StrictInt | None = None
    NextToken: StrictStr | None = None
