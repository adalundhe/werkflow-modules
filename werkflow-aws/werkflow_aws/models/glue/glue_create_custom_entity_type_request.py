from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueCreateCustomEntityTypeRequest(BaseModel):
    Name: StrictStr
    RegexString: StrictStr
    ContextWords: list[StrictStr] | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
