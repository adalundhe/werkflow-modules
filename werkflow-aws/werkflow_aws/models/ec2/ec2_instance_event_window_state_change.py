from __future__ import annotations
from pydantic import BaseModel, StrictStr


class EC2InstanceEventWindowStateChange(BaseModel):
    InstanceEventWindowId: StrictStr | None = None
    State: StrictStr | None = None
