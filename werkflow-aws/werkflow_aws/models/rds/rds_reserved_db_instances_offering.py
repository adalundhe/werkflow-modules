from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .rds_recurring_charge import RDSRecurringCharge


class RDSReservedDBInstancesOffering(BaseModel):
    ReservedDBInstancesOfferingId: StrictStr | None = None
    DBInstanceClass: StrictStr | None = None
    Duration: StrictInt | None = None
    FixedPrice: StrictFloat | StrictInt | None = None
    UsagePrice: StrictFloat | StrictInt | None = None
    CurrencyCode: StrictStr | None = None
    ProductDescription: StrictStr | None = None
    OfferingType: StrictStr | None = None
    MultiAZ: StrictBool | None = None
    RecurringCharges: list[RDSRecurringCharge] | None = None
