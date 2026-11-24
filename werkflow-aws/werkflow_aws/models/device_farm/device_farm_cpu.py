from __future__ import annotations
from pydantic import BaseModel, StrictFloat, StrictInt, StrictStr


class DeviceFarmCPU(BaseModel):
    frequency: StrictStr | None = None
    architecture: StrictStr | None = None
    clock: StrictFloat | StrictInt | None = None
