from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerSourceKeyword(BaseModel):
    keywordInputType: StrictStr | None = None
    keywordValue: StrictStr | None = None
