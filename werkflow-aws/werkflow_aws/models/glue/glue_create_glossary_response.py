from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlueCreateGlossaryResponse(BaseModel):
    Id: StrictStr | None = None
    Name: StrictStr | None = None
    Description: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
