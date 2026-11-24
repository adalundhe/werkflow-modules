from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2ActiveInstance(BaseModel):
    InstanceId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    SpotInstanceRequestId: StrictStr | None = None
    InstanceHealth: StrictStr | None = None
