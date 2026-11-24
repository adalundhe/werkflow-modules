from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr


class ConfigServiceConformancePackComplianceScore(BaseModel):
    Score: StrictStr | None = None
    ConformancePackName: StrictStr | None = None
    LastUpdatedTime: datetime.datetime | StrictStr | None = None
