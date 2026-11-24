from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmListOfferingPromotionsRequest(BaseModel):
    nextToken: StrictStr | None = None
