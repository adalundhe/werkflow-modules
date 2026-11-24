from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .device_farm_monetary_amount import DeviceFarmMonetaryAmount
from .device_farm_offering_status import DeviceFarmOfferingStatus


class DeviceFarmOfferingTransaction(BaseModel):
    offeringStatus: DeviceFarmOfferingStatus | None = None
    transactionId: StrictStr | None = None
    offeringPromotionId: StrictStr | None = None
    createdOn: datetime.datetime | StrictStr | None = None
    cost: DeviceFarmMonetaryAmount | None = None
