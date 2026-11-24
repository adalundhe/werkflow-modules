from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeCatalystGetProjectResponse(BaseModel):
    spaceName: StrictStr | None = None
    name: StrictStr | None = None
    displayName: StrictStr | None = None
    description: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
