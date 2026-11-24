from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_error_detail import GlueErrorDetail


class GlueColumnError(BaseModel):
    ColumnName: StrictStr | None = None
    Error: GlueErrorDetail | None = None
