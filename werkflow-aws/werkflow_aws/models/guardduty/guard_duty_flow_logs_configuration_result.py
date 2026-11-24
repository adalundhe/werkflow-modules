from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GuardDutyFlowLogsConfigurationResult(BaseModel):
    Status: StrictStr | None = None
