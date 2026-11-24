from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2PerformanceFactorReference(BaseModel):
    InstanceFamily: StrictStr | None = None
