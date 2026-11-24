from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr
from .redshift_recurring_charge import RedshiftRecurringCharge


class RedshiftReservedNode(BaseModel):
    ReservedNodeId: StrictStr | None = None
    ReservedNodeOfferingId: StrictStr | None = None
    NodeType: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    Duration: StrictInt | None = None
    FixedPrice: StrictFloat | StrictInt | None = None
    UsagePrice: StrictFloat | StrictInt | None = None
    CurrencyCode: StrictStr | None = None
    NodeCount: StrictInt | None = None
    State: StrictStr | None = None
    OfferingType: StrictStr | None = None
    RecurringCharges: list[RedshiftRecurringCharge] | None = None
    ReservedNodeOfferingType: StrictStr | None = None
