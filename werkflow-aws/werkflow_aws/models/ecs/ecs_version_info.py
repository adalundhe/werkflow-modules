from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSVersionInfo(BaseModel):
    agentVersion: StrictStr | None = None
    agentHash: StrictStr | None = None
    dockerVersion: StrictStr | None = None
