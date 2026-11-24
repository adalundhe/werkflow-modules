from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTStatusReason(BaseModel):
    reasonCode: StrictStr | None = None
    reasonDescription: StrictStr | None = None
