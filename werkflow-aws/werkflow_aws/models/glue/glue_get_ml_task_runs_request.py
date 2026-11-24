from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .glue_task_run_filter_criteria import GlueTaskRunFilterCriteria
from .glue_task_run_sort_criteria import GlueTaskRunSortCriteria


class GlueGetMLTaskRunsRequest(BaseModel):
    TransformId: StrictStr
    NextToken: StrictStr | None = None
    MaxResults: StrictInt | None = None
    Filter: GlueTaskRunFilterCriteria | None = None
    Sort: GlueTaskRunSortCriteria | None = None
