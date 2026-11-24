from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ElastiCacheCustomerNodeEndpoint(BaseModel):
    Address: StrictStr | None = None
    Port: StrictInt | None = None
