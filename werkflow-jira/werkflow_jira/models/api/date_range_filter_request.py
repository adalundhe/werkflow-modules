from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DateRangeFilterRequest(BaseModel):
    dateAfter: StrictStr | None = None
    dateBefore: StrictStr | None = None
