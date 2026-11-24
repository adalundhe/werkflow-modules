from __future__ import annotations
from pydantic import BaseModel, StrictStr


class SecurityLevelMemberPayload(BaseModel):
    parameter: StrictStr | None = None
    type: StrictStr | None = None
