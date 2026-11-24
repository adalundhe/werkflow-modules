from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSDevice(BaseModel):
    hostPath: StrictStr | None = None
    containerPath: StrictStr | None = None
    permissions: list[StrictStr] | None = None
