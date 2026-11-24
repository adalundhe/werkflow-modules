from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppStreamAgentAccessSetting(BaseModel):
    AgentAction: StrictStr | None = None
    Permission: StrictStr | None = None
