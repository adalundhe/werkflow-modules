from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .ec2_purchase import EC2Purchase


class EC2PurchaseHostReservationResponse(BaseModel):
    ClientToken: StrictStr | None = None
    CurrencyCode: StrictStr | None = None
    Purchase: list[EC2Purchase] | None = None
    TotalHourlyPrice: StrictStr | None = None
    TotalUpfrontPrice: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
