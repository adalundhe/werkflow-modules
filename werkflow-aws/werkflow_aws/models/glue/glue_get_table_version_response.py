from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_table_version import GlueTableVersion


class GlueGetTableVersionResponse(BaseModel):
    TableVersion: GlueTableVersion | None = None
    ResponseMetadata: dict[str, Any] | None = None
