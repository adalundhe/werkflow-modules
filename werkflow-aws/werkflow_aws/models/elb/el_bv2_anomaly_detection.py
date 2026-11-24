from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ELBv2AnomalyDetection(BaseModel):
    Result: StrictStr | None = None
    MitigationInEffect: StrictStr | None = None
