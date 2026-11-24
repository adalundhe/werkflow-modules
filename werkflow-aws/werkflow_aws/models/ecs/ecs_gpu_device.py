from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class ECSGpuDevice(BaseModel):
    gpuId: StrictStr | None = None
    sharingMode: StrictStr | None = None
    totalMemoryInMiB: StrictInt | None = None
    remainingMemoryInMiB: StrictInt | None = None
    containerCount: StrictInt | None = None
