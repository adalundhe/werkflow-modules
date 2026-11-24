from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class TimestreamQueryLastUpdate(BaseModel):
    TargetQueryTCU: StrictInt | None = None
    Status: StrictStr | None = None
    StatusMessage: StrictStr | None = None
