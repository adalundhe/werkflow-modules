from __future__ import annotations
from pydantic import BaseModel, StrictStr


class GlueDataQualityEvaluationConfigGlueTables(BaseModel):
    CatalogId: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    TableNamePattern: StrictStr | None = None
    PreProcessingQuery: StrictStr | None = None
    ConnectionName: StrictStr | None = None
    AdditionalOptions: dict[StrictStr, StrictStr] | None = None
