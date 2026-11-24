from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTAuthInfo(BaseModel):
    actionType: StrictStr | None = None
    resources: list[StrictStr] | None = None
