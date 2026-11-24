from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTLogTarget(BaseModel):
    targetType: StrictStr | None = None
    targetName: StrictStr | None = None
