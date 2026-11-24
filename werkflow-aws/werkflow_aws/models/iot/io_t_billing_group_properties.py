from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTBillingGroupProperties(BaseModel):
    billingGroupDescription: StrictStr | None = None
