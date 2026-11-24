from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class CodeCatalystDeleteSpaceResponse(BaseModel):
    name: StrictStr | None = None
    displayName: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
