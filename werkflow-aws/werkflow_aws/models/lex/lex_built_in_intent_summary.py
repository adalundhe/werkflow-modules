from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexBuiltInIntentSummary(BaseModel):
    intentSignature: StrictStr | None = None
    description: StrictStr | None = None
