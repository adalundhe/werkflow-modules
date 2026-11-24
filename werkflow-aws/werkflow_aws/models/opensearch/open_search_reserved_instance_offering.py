from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .open_search_recurring_charge import OpenSearchRecurringCharge


class OpenSearchReservedInstanceOffering(BaseModel):
    ReservedInstanceOfferingId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    Duration: StrictInt | None = None
    FixedPrice: StrictFloat | StrictInt | None = None
    UsagePrice: StrictFloat | StrictInt | None = None
    CurrencyCode: StrictStr | None = None
    PaymentOption: StrictStr | None = None
    RecurringCharges: list[OpenSearchRecurringCharge] | None = None
