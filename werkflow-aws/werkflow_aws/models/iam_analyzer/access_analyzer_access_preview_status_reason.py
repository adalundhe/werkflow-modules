from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerAccessPreviewStatusReason(BaseModel):
    code: StrictStr | None = None
