from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_workflow_run import GlueWorkflowRun


class GlueGetWorkflowRunResponse(BaseModel):
    Run: GlueWorkflowRun | None = None
    ResponseMetadata: dict[str, Any] | None = None
