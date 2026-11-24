from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .glue_table_optimizer import GlueTableOptimizer


class GlueBatchTableOptimizer(BaseModel):
    catalogId: StrictStr | None = None
    databaseName: StrictStr | None = None
    tableName: StrictStr | None = None
    tableOptimizer: GlueTableOptimizer | None = None
