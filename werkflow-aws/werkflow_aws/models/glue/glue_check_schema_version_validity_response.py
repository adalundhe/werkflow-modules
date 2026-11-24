from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr


class GlueCheckSchemaVersionValidityResponse(BaseModel):
    Valid: StrictBool | None = None
    Error: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
