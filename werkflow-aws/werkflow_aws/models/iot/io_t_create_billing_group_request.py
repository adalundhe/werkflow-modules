from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .io_t_billing_group_properties import IoTBillingGroupProperties
from .io_t_tag import IoTTag


class IoTCreateBillingGroupRequest(BaseModel):
    billingGroupName: StrictStr
    billingGroupProperties: IoTBillingGroupProperties | None = None
    tags: list[IoTTag] | None = None
