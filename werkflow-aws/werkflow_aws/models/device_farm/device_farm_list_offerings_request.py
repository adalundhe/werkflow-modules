from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmListOfferingsRequest(BaseModel):
    nextToken: StrictStr | None = None
