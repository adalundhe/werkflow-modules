from __future__ import annotations
from pydantic import BaseModel, StrictBool
from .ecs_device import ECSDevice
from .ecs_kernel_capabilities import ECSKernelCapabilities
from .ecs_tmpfs import ECSTmpfs


class ECSDaemonLinuxParameters(BaseModel):
    capabilities: ECSKernelCapabilities | None = None
    devices: list[ECSDevice] | None = None
    initProcessEnabled: StrictBool | None = None
    tmpfs: list[ECSTmpfs] | None = None
