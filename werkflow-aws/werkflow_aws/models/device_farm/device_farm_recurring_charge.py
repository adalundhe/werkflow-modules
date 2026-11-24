from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .device_farm_monetary_amount import DeviceFarmMonetaryAmount


class DeviceFarmRecurringCharge(BaseModel):
    cost: DeviceFarmMonetaryAmount | None = None
    frequency: StrictStr | None = None
