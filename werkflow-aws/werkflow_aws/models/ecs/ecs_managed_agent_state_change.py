from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class ECSManagedAgentStateChange(BaseModel):
    containerName: StrictStr
    managedAgentName: Literal['ExecuteCommandAgent']
    status: StrictStr
    reason: StrictStr | None = None
