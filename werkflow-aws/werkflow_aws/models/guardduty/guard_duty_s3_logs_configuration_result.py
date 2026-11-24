from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyS3LogsConfigurationResult(BaseModel):
    Status: StrictStr | None = None
