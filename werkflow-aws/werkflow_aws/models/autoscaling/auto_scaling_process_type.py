from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AutoScalingProcessType(BaseModel):
    ProcessName: StrictStr | None = None
