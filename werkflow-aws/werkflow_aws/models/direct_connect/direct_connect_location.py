from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .direct_connect_available_billing_mode import DirectConnectAvailableBillingMode


class DirectConnectLocation(BaseModel):
    locationCode: StrictStr | None = None
    locationName: StrictStr | None = None
    region: StrictStr | None = None
    availablePortSpeeds: list[StrictStr] | None = None
    availableProviders: list[StrictStr] | None = None
    availableMacSecPortSpeeds: list[StrictStr] | None = None
    availableBillingModes: list[DirectConnectAvailableBillingMode] | None = None
