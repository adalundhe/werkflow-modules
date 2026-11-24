from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueCustomEntityType(BaseModel):
    Name: StrictStr | None = None
    RegexString: StrictStr | None = None
    ContextWords: list[StrictStr] | None = None
