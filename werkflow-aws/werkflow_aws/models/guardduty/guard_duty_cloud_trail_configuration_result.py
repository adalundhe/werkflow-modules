from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyCloudTrailConfigurationResult(BaseModel):
    Status: StrictStr | None = None
