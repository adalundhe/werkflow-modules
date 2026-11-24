from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .ssm_severity_summary import SSMSeveritySummary


class SSMNonCompliantSummary(BaseModel):
    NonCompliantCount: StrictInt | None = None
    SeveritySummary: SSMSeveritySummary | None = None
