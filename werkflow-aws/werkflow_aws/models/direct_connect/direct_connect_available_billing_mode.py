from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectConnectAvailableBillingMode(BaseModel):
    billingMode: StrictStr | None = None
    availablePortSpeeds: list[StrictStr] | None = None
    includedRegions: list[StrictStr] | None = None
