from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TimeTrackingProvider(BaseModel):
    key: StrictStr | None = None
    name: StrictStr | None = None
    url: StrictStr | None = None
