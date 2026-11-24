from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDataQualityEvaluationConfigListGlueTables(BaseModel):
    CatalogId: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    TableNamePattern: StrictStr | None = None
