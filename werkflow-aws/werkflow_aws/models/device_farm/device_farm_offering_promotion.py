from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmOfferingPromotion(BaseModel):
    id: StrictStr | None = None
    description: StrictStr | None = None
