from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class SageMakerAgentVersion(BaseModel):
    Version: StrictStr | None = None
    AgentCount: StrictInt | None = None
