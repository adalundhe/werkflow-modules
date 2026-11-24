from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlueGetCustomEntityTypeResponse(BaseModel):
    Name: StrictStr | None = None
    RegexString: StrictStr | None = None
    ContextWords: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
