from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .redshift_recurring_charge import RedshiftRecurringCharge


class RedshiftReservedNodeOffering(BaseModel):
    ReservedNodeOfferingId: StrictStr | None = None
    NodeType: StrictStr | None = None
    Duration: StrictInt | None = None
    FixedPrice: StrictFloat | StrictInt | None = None
    UsagePrice: StrictFloat | StrictInt | None = None
    CurrencyCode: StrictStr | None = None
    OfferingType: StrictStr | None = None
    RecurringCharges: list[RedshiftRecurringCharge] | None = None
    ReservedNodeOfferingType: StrictStr | None = None
