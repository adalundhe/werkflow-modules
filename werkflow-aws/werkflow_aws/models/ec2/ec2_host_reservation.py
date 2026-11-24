from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .ec2_tag_model import EC2TagModel


class EC2HostReservation(BaseModel):
    Count: StrictInt | None = None
    CurrencyCode: StrictStr | None = None
    Duration: StrictInt | None = None
    End: datetime.datetime | StrictStr | None = None
    HostIdSet: list[StrictStr] | None = None
    HostReservationId: StrictStr | None = None
    HourlyPrice: StrictStr | None = None
    InstanceFamily: StrictStr | None = None
    OfferingId: StrictStr | None = None
    PaymentOption: StrictStr | None = None
    Start: datetime.datetime | StrictStr | None = None
    State: StrictStr | None = None
    UpfrontPrice: StrictStr | None = None
    Tags: list[EC2TagModel] | None = None
