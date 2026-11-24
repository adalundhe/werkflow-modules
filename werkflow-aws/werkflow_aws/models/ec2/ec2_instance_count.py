from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EC2InstanceCount(BaseModel):
    InstanceCount: StrictInt | None = None
    State: StrictStr | None = None
