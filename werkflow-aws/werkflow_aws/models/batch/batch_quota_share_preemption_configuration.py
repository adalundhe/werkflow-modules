from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchQuotaSharePreemptionConfiguration(BaseModel):
    inSharePreemption: StrictStr | None = None
