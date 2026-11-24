from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2Purchase(BaseModel):
    CurrencyCode: StrictStr | None = None
    Duration: StrictInt | None = None
    HostIdSet: list[StrictStr] | None = None
    HostReservationId: StrictStr | None = None
    HourlyPrice: StrictStr | None = None
    InstanceFamily: StrictStr | None = None
    PaymentOption: StrictStr | None = None
    UpfrontPrice: StrictStr | None = None
