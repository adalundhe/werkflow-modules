from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexIssueLocation(BaseModel):
    botLocale: StrictStr | None = None
    intentId: StrictStr | None = None
    slotId: StrictStr | None = None
