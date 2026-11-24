from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_catalyst_workflow_run_summary import CodeCatalystWorkflowRunSummary


class CodeCatalystListWorkflowRunsResponse(BaseModel):
    nextToken: StrictStr | None = None
    items: list[CodeCatalystWorkflowRunSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
