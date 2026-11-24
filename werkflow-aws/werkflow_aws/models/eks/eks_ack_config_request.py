from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class EKSAckConfigRequest(BaseModel):
    enableCrossNamespace: StrictBool | None = None
    disabledServices: list[StrictStr] | None = None
