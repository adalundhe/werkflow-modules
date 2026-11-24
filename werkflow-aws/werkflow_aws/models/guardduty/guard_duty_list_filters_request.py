from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class GuardDutyListFiltersRequest(BaseModel):
    DetectorId: StrictStr
    MaxResults: StrictInt | None = None
    NextToken: StrictStr | None = None
