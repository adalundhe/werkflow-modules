from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class RedshiftRecurringCharge(BaseModel):
    RecurringChargeAmount: StrictFloat | StrictInt | None = None
    RecurringChargeFrequency: StrictStr | None = None
