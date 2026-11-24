from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class CodeBuildComputeConfiguration(BaseModel):
    vCpu: StrictInt | None = None
    memory: StrictInt | None = None
    disk: StrictInt | None = None
    machineType: StrictStr | None = None
    instanceType: StrictStr | None = None
