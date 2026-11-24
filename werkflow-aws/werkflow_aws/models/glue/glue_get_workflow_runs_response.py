from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_workflow_run import GlueWorkflowRun


class GlueGetWorkflowRunsResponse(BaseModel):
    Runs: list[GlueWorkflowRun] | None = None
    NextToken: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
