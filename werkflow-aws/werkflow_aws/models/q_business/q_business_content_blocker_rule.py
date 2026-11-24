from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessContentBlockerRule(BaseModel):
    systemMessageOverride: StrictStr | None = None
