from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyAgentDetails(BaseModel):
    Version: StrictStr | None = None
