from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr


class AccessAnalyzerReasonSummary(BaseModel):
    description: StrictStr | None = None
    statementIndex: StrictInt | None = None
    statementId: StrictStr | None = None
