from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSSession(BaseModel):
    sessionId: StrictStr | None = None
    streamUrl: StrictStr | None = None
    tokenValue: StrictStr | None = None
