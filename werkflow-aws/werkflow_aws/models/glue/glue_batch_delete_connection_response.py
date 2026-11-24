from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_error_detail import GlueErrorDetail


class GlueBatchDeleteConnectionResponse(BaseModel):
    Succeeded: list[StrictStr] | None = None
    Errors: dict[StrictStr, GlueErrorDetail] | None = None
    ResponseMetadata: dict[str, Any] | None = None
