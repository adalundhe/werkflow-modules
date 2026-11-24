from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmProblemDetail(BaseModel):
    arn: StrictStr | None = None
    name: StrictStr | None = None
