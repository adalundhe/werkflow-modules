from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class DirectoryServiceCreateAliasResponse(BaseModel):
    DirectoryId: StrictStr | None = None
    Alias: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
