from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SSMCancelCommandRequest(BaseModel):
    CommandId: StrictStr
    InstanceIds: list[StrictStr] | None = None
