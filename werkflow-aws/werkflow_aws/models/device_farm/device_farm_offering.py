from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .device_farm_recurring_charge import DeviceFarmRecurringCharge


class DeviceFarmOffering(BaseModel):
    id: StrictStr | None = None
    description: StrictStr | None = None
    type: StrictStr | None = None
    platform: StrictStr | None = None
    recurringCharges: list[DeviceFarmRecurringCharge] | None = None
