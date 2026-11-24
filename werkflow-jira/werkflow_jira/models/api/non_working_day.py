from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class NonWorkingDay(BaseModel):
    id: StrictInt | None = None
    iso8601Date: StrictStr | None = None
