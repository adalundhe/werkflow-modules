from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictFloat, StrictInt, StrictStr
from .rds_recurring_charge import RDSRecurringCharge


class RDSReservedDBInstance(BaseModel):
    ReservedDBInstanceId: StrictStr | None = None
    ReservedDBInstancesOfferingId: StrictStr | None = None
    DBInstanceClass: StrictStr | None = None
    StartTime: datetime.datetime | StrictStr | None = None
    Duration: StrictInt | None = None
    FixedPrice: StrictFloat | StrictInt | None = None
    UsagePrice: StrictFloat | StrictInt | None = None
    CurrencyCode: StrictStr | None = None
    DBInstanceCount: StrictInt | None = None
    ProductDescription: StrictStr | None = None
    OfferingType: StrictStr | None = None
    MultiAZ: StrictBool | None = None
    State: StrictStr | None = None
    RecurringCharges: list[RDSRecurringCharge] | None = None
    ReservedDBInstanceArn: StrictStr | None = None
    LeaseId: StrictStr | None = None
