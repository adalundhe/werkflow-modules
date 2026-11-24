from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectApproximateDriftedResourceCount(BaseModel):
    Region: StrictStr | None = None
    Count: StrictInt | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
