from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .io_t_billing_group_properties import IoTBillingGroupProperties


class IoTUpdateBillingGroupRequest(BaseModel):
    billingGroupName: StrictStr
    billingGroupProperties: IoTBillingGroupProperties
    expectedVersion: StrictInt | None = None
