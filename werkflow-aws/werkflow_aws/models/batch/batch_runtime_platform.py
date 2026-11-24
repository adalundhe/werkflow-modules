from __future__ import annotations
from pydantic import BaseModel, StrictStr


class BatchRuntimePlatform(BaseModel):
    operatingSystemFamily: StrictStr | None = None
    cpuArchitecture: StrictStr | None = None
