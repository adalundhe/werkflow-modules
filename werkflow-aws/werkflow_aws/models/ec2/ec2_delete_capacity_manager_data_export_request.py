from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EC2DeleteCapacityManagerDataExportRequest(BaseModel):
    CapacityManagerDataExportId: StrictStr
    DryRun: StrictBool | None = None
