from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_table_error import GlueTableError


class GlueBatchDeleteTableResponse(BaseModel):
    Errors: list[GlueTableError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
