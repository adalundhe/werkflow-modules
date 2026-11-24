from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr


class EC2ModifyInstanceCpuOptionsRequest(BaseModel):
    InstanceId: StrictStr
    CoreCount: StrictInt | None = None
    ThreadsPerCore: StrictInt | None = None
    NestedVirtualization: Literal['enabled', 'disabled'] | None = None
    DryRun: StrictBool | None = None
