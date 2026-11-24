from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SWFDomainConfiguration(BaseModel):
    workflowExecutionRetentionPeriodInDays: StrictStr | None = None
