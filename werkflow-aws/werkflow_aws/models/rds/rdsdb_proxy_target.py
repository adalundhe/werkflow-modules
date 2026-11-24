from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .rds_target_health import RDSTargetHealth


class RDSDBProxyTarget(BaseModel):
    TargetArn: StrictStr | None = None
    Endpoint: StrictStr | None = None
    TrackedClusterId: StrictStr | None = None
    RdsResourceId: StrictStr | None = None
    Port: StrictInt | None = None
    Type: StrictStr | None = None
    Role: StrictStr | None = None
    TargetHealth: RDSTargetHealth | None = None
