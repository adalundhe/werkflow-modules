from __future__ import annotations
from pydantic import BaseModel
from .glue_data_quality_glue_table import GlueDataQualityGlueTable
from .glue_table import GlueTable as _GlueTableType


class GlueDataSource(BaseModel):
    GlueTable: _GlueTableType | None = None
    DataQualityGlueTable: GlueDataQualityGlueTable | None = None
