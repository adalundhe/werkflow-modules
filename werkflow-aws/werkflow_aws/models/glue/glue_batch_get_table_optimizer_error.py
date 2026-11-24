from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_error_detail import GlueErrorDetail


class GlueBatchGetTableOptimizerError(BaseModel):
    error: GlueErrorDetail | None = None
    catalogId: StrictStr | None = None
    databaseName: StrictStr | None = None
    tableName: StrictStr | None = None
    type: StrictStr | None = None
