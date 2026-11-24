from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_batch_get_table_optimizer_error import GlueBatchGetTableOptimizerError
from .glue_batch_table_optimizer import GlueBatchTableOptimizer


class GlueBatchGetTableOptimizerResponse(BaseModel):
    TableOptimizers: list[GlueBatchTableOptimizer] | None = None
    Failures: list[GlueBatchGetTableOptimizerError] | None = None
    ResponseMetadata: dict[str, Any] | None = None
