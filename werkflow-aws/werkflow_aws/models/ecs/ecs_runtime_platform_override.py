from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSRuntimePlatformOverride(BaseModel):
    cpuArchitecture: StrictStr | None = None
