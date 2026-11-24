from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class SecurityHubUpdateStandardsControlRequest(BaseModel):
    StandardsControlArn: StrictStr
    ControlStatus: Literal['ENABLED', 'DISABLED'] | None = None
    DisabledReason: StrictStr | None = None
