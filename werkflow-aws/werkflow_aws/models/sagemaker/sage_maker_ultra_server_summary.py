from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerUltraServerSummary(BaseModel):
    UltraServerType: StrictStr | None = None
    InstanceType: StrictStr | None = None
    UltraServerCount: StrictInt | None = None
    AvailableSpareInstanceCount: StrictInt | None = None
    UnhealthyInstanceCount: StrictInt | None = None
