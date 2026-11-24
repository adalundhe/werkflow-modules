from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictInt, StrictStr
from .io_t_billing_group_metadata import IoTBillingGroupMetadata
from .io_t_billing_group_properties import IoTBillingGroupProperties


class IoTDescribeBillingGroupResponse(BaseModel):
    billingGroupName: StrictStr | None = None
    billingGroupId: StrictStr | None = None
    billingGroupArn: StrictStr | None = None
    version: StrictInt | None = None
    billingGroupProperties: IoTBillingGroupProperties | None = None
    billingGroupMetadata: IoTBillingGroupMetadata | None = None
    ResponseMetadata: dict[str, Any] | None = None
