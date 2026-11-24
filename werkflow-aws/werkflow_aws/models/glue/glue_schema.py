from __future__ import annotations
from pydantic import BaseModel
from .glue_studio_schema_column import GlueStudioSchemaColumn


class GlueSchema(BaseModel):
    Columns: list[GlueStudioSchemaColumn] | None = None
