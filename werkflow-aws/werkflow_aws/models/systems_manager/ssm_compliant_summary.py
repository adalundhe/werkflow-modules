from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .ssm_severity_summary import SSMSeveritySummary


class SSMCompliantSummary(BaseModel):
    CompliantCount: StrictInt | None = None
    SeveritySummary: SSMSeveritySummary | None = None
