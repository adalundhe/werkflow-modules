from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyIncrementalScanDetails(BaseModel):
    BaselineResourceArn: StrictStr | None = None
