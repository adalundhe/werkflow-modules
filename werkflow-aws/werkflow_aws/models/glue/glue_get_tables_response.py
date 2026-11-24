from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_table_model import GlueTableModel


class GlueGetTablesResponse(BaseModel):
    TableList: list[GlueTableModel] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
