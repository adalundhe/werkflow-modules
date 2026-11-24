from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LexRecommendedIntentSummary(BaseModel):
    intentId: StrictStr | None = None
    intentName: StrictStr | None = None
    sampleUtterancesCount: StrictInt | None = None
