from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_table_optimizer_run import GlueTableOptimizerRun


class GlueListTableOptimizerRunsResponse(BaseModel):
    CatalogId: StrictStr | None = None
    DatabaseName: StrictStr | None = None
    TableName: StrictStr | None = None
    NextToken: StrictStr | None = None
    TableOptimizerRuns: list[GlueTableOptimizerRun] | None = None
    ResponseMetadata: dict[str, Any] | None = None
