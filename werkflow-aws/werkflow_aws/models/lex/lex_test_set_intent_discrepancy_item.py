from __future__ import annotations
from pydantic import BaseModel, StrictStr


class LexTestSetIntentDiscrepancyItem(BaseModel):
    intentName: StrictStr | None = None
    errorMessage: StrictStr | None = None
