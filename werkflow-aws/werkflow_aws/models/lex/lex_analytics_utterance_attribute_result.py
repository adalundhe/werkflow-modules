from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexAnalyticsUtteranceAttributeResult(BaseModel):
    lastUsedIntent: StrictStr | None = None
