from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class EMRInstanceResizePolicy(BaseModel):
    InstancesToTerminate: list[StrictStr] | None = None
    InstancesToProtect: list[StrictStr] | None = None
    InstanceTerminationTimeout: StrictInt | None = None
