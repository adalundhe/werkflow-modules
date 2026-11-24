from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class Route53StatusReport(BaseModel):
    Status: StrictStr | None = None
    CheckedTime: datetime.datetime | None = None
