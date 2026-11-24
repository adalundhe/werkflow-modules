from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt
from .batch_device import BatchDevice
from .batch_tmpfs import BatchTmpfs


class BatchLinuxParameters(BaseModel):
    devices: list[BatchDevice] | None = None
    initProcessEnabled: StrictBool | None = None
    sharedMemorySize: StrictInt | None = None
    tmpfs: list[BatchTmpfs] | None = None
    maxSwap: StrictInt | None = None
    swappiness: StrictInt | None = None
