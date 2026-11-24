from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConfigServiceConformancePackComplianceSummary(BaseModel):
    ConformancePackName: StrictStr | None = None
    ConformancePackComplianceStatus: StrictStr | None = None
