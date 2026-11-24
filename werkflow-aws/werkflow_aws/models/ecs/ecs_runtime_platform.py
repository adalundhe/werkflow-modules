from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSRuntimePlatform(BaseModel):
    cpuArchitecture: StrictStr | None = None
    operatingSystemFamily: StrictStr | None = None
