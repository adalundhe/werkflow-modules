from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexInvokedIntentSample(BaseModel):
    intentName: StrictStr | None = None
