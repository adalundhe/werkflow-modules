from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerUltraServer(BaseModel):
    UltraServerId: StrictStr | None = None
    UltraServerType: StrictStr | None = None
    AvailabilityZone: StrictStr | None = None
    InstanceType: StrictStr | None = None
    TotalInstanceCount: StrictInt | None = None
    ConfiguredSpareInstanceCount: StrictInt | None = None
    AvailableInstanceCount: StrictInt | None = None
    InUseInstanceCount: StrictInt | None = None
    AvailableSpareInstanceCount: StrictInt | None = None
    UnhealthyInstanceCount: StrictInt | None = None
    HealthStatus: StrictStr | None = None
