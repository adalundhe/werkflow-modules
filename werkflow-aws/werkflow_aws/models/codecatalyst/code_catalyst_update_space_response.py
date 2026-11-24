from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeCatalystUpdateSpaceResponse(BaseModel):
    name: StrictStr | None = None
    displayName: StrictStr | None = None
    description: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
