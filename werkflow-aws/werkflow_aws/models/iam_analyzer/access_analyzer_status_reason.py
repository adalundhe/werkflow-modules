from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerStatusReason(BaseModel):
    code: StrictStr | None = None
