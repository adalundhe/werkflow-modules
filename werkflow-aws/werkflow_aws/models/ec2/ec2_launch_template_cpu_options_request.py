from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt


class EC2LaunchTemplateCpuOptionsRequest(BaseModel):
    CoreCount: StrictInt | None = None
    ThreadsPerCore: StrictInt | None = None
    AmdSevSnp: Literal['enabled', 'disabled'] | None = None
    NestedVirtualization: Literal['enabled', 'disabled'] | None = None
