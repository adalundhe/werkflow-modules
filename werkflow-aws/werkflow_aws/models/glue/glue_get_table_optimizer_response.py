from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_table_optimizer import GlueTableOptimizer


class GlueGetTableOptimizerResponse(BaseModel):
    CatalogId: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    TableName: StrictStr | None = None
    TableOptimizer: GlueTableOptimizer | None = None
    ResponseMetadata: dict[str, Any] | None = None
