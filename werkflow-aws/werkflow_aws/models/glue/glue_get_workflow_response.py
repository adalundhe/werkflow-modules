from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .glue_workflow import GlueWorkflow


class GlueGetWorkflowResponse(BaseModel):
    Workflow: GlueWorkflow | None = None
    ResponseMetadata: dict[str, Any] | None = None
