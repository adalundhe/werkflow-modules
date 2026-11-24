from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmGetOfferingStatusRequest(BaseModel):
    nextToken: StrictStr | None = None
