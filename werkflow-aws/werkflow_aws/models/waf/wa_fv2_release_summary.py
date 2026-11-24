from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class WAFv2ReleaseSummary(BaseModel):
    ReleaseVersion: StrictStr | None = None
    Timestamp: datetime.datetime | StrictStr | None = None
