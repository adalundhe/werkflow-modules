from __future__ import annotations
from pydantic import BaseModel, StrictStr


class STSScopedSession(BaseModel):
    ScopedSessionId: StrictStr | None = None
    Arn: StrictStr | None = None
