from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerComputeQuotaTarget(BaseModel):
    TeamName: StrictStr | None = None
    FairShareWeight: StrictInt | None = None
