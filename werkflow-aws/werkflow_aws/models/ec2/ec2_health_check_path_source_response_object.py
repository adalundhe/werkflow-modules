from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2HealthCheckPathSourceResponseObject(BaseModel):
    SubnetId: StrictStr | None = None
    SecurityGroupId: StrictStr | None = None
