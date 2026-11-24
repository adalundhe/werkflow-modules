from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlueCreateGlossaryTermResponse(BaseModel):
    Id: StrictStr | None = None
    GlossaryId: StrictStr | None = None
    Name: StrictStr | None = None
    ShortDescription: StrictStr | None = None
    LongDescription: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
