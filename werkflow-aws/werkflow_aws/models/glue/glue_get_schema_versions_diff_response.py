from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class GlueGetSchemaVersionsDiffResponse(BaseModel):
    Diff: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
