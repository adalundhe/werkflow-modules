from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerGetAccessPreviewRequest(BaseModel):
    accessPreviewId: StrictStr
    analyzerArn: StrictStr
