from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PinpointCustomDeliveryConfiguration(BaseModel):
    DeliveryUri: StrictStr | None = None
    EndpointTypes: list[StrictStr] | None = None
