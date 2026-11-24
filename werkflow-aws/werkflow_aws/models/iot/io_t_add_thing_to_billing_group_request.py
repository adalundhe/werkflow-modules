from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTAddThingToBillingGroupRequest(BaseModel):
    billingGroupName: StrictStr | None = None
    billingGroupArn: StrictStr | None = None
    thingName: StrictStr | None = None
    thingArn: StrictStr | None = None
