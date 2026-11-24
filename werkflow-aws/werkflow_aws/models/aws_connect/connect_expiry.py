from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr


class ConnectExpiry(BaseModel):
    DurationInSeconds: StrictInt | None = None
    ExpiryTimestamp: datetime.datetime | StrictStr | None = None
