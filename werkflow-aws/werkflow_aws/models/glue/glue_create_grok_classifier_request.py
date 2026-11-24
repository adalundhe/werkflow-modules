from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueCreateGrokClassifierRequest(BaseModel):
    Classification: StrictStr
    Name: StrictStr
    GrokPattern: StrictStr
    CustomPatterns: StrictStr | None = None
