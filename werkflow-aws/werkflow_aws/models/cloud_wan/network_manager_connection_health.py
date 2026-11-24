from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class NetworkManagerConnectionHealth(BaseModel):
    Type: StrictStr | None = None
    Status: StrictStr | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
