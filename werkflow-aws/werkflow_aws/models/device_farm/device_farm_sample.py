from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmSample(BaseModel):
    arn: StrictStr | None = None
    type: StrictStr | None = None
    url: StrictStr | None = None
