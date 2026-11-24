from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerDeleteAnalyzerRequest(BaseModel):
    analyzerName: StrictStr
    clientToken: StrictStr | None = None
