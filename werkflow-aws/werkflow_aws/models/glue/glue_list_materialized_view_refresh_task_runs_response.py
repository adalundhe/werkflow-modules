from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_materialized_view_refresh_task_run import GlueMaterializedViewRefreshTaskRun


class GlueListMaterializedViewRefreshTaskRunsResponse(BaseModel):
    MaterializedViewRefreshTaskRuns: list[GlueMaterializedViewRefreshTaskRun] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
