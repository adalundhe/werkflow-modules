from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyCloudDetails(BaseModel):
    Provider: StrictStr | None = None
    Region: StrictStr | None = None
    Account: StrictStr | None = None
