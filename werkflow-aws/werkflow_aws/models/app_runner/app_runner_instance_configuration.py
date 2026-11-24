from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppRunnerInstanceConfiguration(BaseModel):
    Cpu: StrictStr | None = None
    Memory: StrictStr | None = None
    InstanceRoleArn: StrictStr | None = None
