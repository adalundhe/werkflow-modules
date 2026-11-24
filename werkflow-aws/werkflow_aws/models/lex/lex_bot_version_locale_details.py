from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexBotVersionLocaleDetails(BaseModel):
    sourceBotVersion: StrictStr | None = None
