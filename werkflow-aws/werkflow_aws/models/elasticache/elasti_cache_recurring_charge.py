from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class ElastiCacheRecurringCharge(BaseModel):
    RecurringChargeAmount: StrictFloat | StrictInt | None = None
    RecurringChargeFrequency: StrictStr | None = None
