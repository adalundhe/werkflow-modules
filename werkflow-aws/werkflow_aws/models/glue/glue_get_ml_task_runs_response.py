from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_task_run import GlueTaskRun


class GlueGetMLTaskRunsResponse(BaseModel):
    TaskRuns: list[GlueTaskRun] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
