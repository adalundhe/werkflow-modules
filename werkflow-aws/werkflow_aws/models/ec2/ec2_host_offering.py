from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2HostOffering(BaseModel):
    CurrencyCode: StrictStr | None = None
    Duration: StrictInt | None = None
    HourlyPrice: StrictStr | None = None
    InstanceFamily: StrictStr | None = None
    OfferingId: StrictStr | None = None
    PaymentOption: StrictStr | None = None
    UpfrontPrice: StrictStr | None = None
