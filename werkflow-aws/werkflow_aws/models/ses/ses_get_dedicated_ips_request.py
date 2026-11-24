from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SESGetDedicatedIpsRequest(BaseModel):
    PoolName: StrictStr | None = None
    NextToken: StrictStr | None = None
    PageSize: StrictInt | None = None
