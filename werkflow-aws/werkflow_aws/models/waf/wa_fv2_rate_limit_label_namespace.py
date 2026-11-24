from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WAFv2RateLimitLabelNamespace(BaseModel):
    Namespace: StrictStr | None = None
