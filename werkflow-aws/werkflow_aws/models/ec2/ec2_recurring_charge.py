from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class EC2RecurringCharge(BaseModel):
    Amount: StrictFloat | StrictInt | None = None
    Frequency: StrictStr | None = None
