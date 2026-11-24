from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class LexAnalyticsIntentNodeSummary(BaseModel):
    intentName: StrictStr | None = None
    intentPath: StrictStr | None = None
    intentCount: StrictInt | None = None
    intentLevel: StrictInt | None = None
    nodeType: StrictStr | None = None
