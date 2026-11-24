from __future__ import annotations
from pydantic import BaseModel
from .glue_cursor_configuration import GlueCursorConfiguration
from .glue_offset_configuration import GlueOffsetConfiguration


class GluePaginationConfiguration(BaseModel):
    CursorConfiguration: GlueCursorConfiguration | None = None
    OffsetConfiguration: GlueOffsetConfiguration | None = None
