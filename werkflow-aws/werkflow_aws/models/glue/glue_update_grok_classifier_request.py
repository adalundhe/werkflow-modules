from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueUpdateGrokClassifierRequest(BaseModel):
    Name: StrictStr
    Classification: StrictStr | None = None
    GrokPattern: StrictStr | None = None
    CustomPatterns: StrictStr | None = None
