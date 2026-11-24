from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerDeleteServiceLinkedAnalyzerRequest(BaseModel):
    analyzerName: StrictStr
    clientToken: StrictStr | None = None
