from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .glue_workflow import GlueWorkflow


class GlueBatchGetWorkflowsResponse(BaseModel):
    Workflows: list[GlueWorkflow] | None = None
    MissingWorkflows: list[StrictStr] | None = None
    ResponseMetadata: dict[str, Any] | None = None
