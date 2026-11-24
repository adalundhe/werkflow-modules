from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_table_version_error import GlueTableVersionError


class GlueBatchDeleteTableVersionResponse(BaseModel):
    Errors: list[GlueTableVersionError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
