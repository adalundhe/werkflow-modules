from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .device_farm_offering_transaction import DeviceFarmOfferingTransaction


class DeviceFarmRenewOfferingResponse(BaseModel):
    offeringTransaction: DeviceFarmOfferingTransaction | None = None
    ResponseMetadata: dict[str, Any] | None = None
