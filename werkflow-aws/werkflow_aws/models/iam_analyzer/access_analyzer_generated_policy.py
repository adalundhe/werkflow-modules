from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AccessAnalyzerGeneratedPolicy(BaseModel):
    policy: StrictStr | None = None
