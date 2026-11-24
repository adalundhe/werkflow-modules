from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AuditManagerURL(BaseModel):
    hyperlinkName: StrictStr | None = None
    link: StrictStr | None = None
