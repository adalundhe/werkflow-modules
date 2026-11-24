from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TimestreamQueryEndpoint(BaseModel):
    Address: StrictStr | None = None
    CachePeriodInMinutes: StrictInt | None = None
