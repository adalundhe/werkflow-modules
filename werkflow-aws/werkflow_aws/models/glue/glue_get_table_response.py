from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_table_model import GlueTableModel


class GlueGetTableResponse(BaseModel):
    Table: GlueTableModel | None = None
    ResponseMetadata: dict[str, Any] | None = None
