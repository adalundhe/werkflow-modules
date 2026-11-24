from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_materialized_view_refresh_task_run import GlueMaterializedViewRefreshTaskRun


class GlueGetMaterializedViewRefreshTaskRunResponse(BaseModel):
    MaterializedViewRefreshTaskRun: GlueMaterializedViewRefreshTaskRun | None = None
    ResponseMetadata: dict[str, Any] | None = None
