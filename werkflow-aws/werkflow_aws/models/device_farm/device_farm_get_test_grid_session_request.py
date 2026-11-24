from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DeviceFarmGetTestGridSessionRequest(BaseModel):
    projectArn: StrictStr | None = None
    sessionId: StrictStr | None = None
    sessionArn: StrictStr | None = None
