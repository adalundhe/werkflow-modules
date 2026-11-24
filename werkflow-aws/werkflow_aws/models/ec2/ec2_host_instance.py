from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2HostInstance(BaseModel):
    InstanceId: StrictStr | None = None
    InstanceType: StrictStr | None = None
    OwnerId: StrictStr | None = None
