from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .device_farm_offering_promotion import DeviceFarmOfferingPromotion


class DeviceFarmListOfferingPromotionsResponse(BaseModel):
    offeringPromotions: list[DeviceFarmOfferingPromotion] | None = None
    nextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
