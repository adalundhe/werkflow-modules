from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyScanResultDetails(BaseModel):
    ScanResult: StrictStr | None = None
