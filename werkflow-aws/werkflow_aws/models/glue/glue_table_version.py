from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_table_model import GlueTableModel


class GlueTableVersion(BaseModel):
    Table: GlueTableModel | None = None
    VersionId: StrictStr | None = None
