from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictInt
from .ecs_device import ECSDevice
from .ecs_kernel_capabilities import ECSKernelCapabilities
from .ecs_tmpfs import ECSTmpfs


class ECSLinuxParameters(BaseModel):
    capabilities: ECSKernelCapabilities | None = None
    devices: list[ECSDevice] | None = None
    initProcessEnabled: StrictBool | None = None
    sharedMemorySize: StrictInt | None = None
    tmpfs: list[ECSTmpfs] | None = None
    maxSwap: StrictInt | None = None
    swappiness: StrictInt | None = None
