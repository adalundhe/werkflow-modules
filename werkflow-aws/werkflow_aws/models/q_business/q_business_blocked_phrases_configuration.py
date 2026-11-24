from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QBusinessBlockedPhrasesConfiguration(BaseModel):
    blockedPhrases: list[StrictStr] | None = None
    systemMessageOverride: StrictStr | None = None
