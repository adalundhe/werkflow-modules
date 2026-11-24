from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TimestreamWriteEndpoint(BaseModel):
    Address: StrictStr | None = None
    CachePeriodInMinutes: StrictInt | None = None
