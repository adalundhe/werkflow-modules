from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EndUserMessagingCarrierStatusInformation(BaseModel):
    CarrierName: StrictStr | None = None
    Status: StrictStr | None = None
