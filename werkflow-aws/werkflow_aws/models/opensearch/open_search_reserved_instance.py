from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .open_search_recurring_charge import OpenSearchRecurringCharge


class OpenSearchReservedInstance(BaseModel):
    ReservationName: StrictStr | None = None
    ReservedInstanceId: StrictStr | None = None
    BillingSubscriptionId: StrictInt | None = None
    ReservedInstanceOfferingId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    Duration: StrictInt | None = None
    FixedPrice: StrictFloat | StrictInt | None = None
    UsagePrice: StrictFloat | StrictInt | None = None
    CurrencyCode: StrictStr | None = None
    InstanceCount: StrictInt | None = None
    State: StrictStr | None = None
    PaymentOption: StrictStr | None = None
    RecurringCharges: list[OpenSearchRecurringCharge] | None = None
