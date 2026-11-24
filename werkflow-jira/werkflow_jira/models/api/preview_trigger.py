from __future__ import annotations
from pydantic import BaseModel, StrictStr


class PreviewTrigger(BaseModel):
    id: StrictStr | None = None
    ruleKey: StrictStr | None = None
