from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class IoTCreateBillingGroupResponse(BaseModel):
    billingGroupName: StrictStr | None = None
    billingGroupArn: StrictStr | None = None
    billingGroupId: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
