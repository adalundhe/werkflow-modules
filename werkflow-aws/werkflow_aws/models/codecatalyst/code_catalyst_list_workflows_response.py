from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_catalyst_workflow_summary import CodeCatalystWorkflowSummary


class CodeCatalystListWorkflowsResponse(BaseModel):
    nextToken: StrictStr | None = None
    items: list[CodeCatalystWorkflowSummary] | None = None
    ResponseMetadata: dict[str, Any] | None = None
