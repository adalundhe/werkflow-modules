from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2HealthCheckPathSourceRequestObject(BaseModel):
    SubnetId: StrictStr | None = None
    SecurityGroupId: StrictStr | None = None
