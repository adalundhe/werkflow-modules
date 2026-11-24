from __future__ import annotations
from pydantic import BaseModel, StrictStr


class TextractGetDocumentInsightsRequest(BaseModel):
    JobArn: StrictStr
