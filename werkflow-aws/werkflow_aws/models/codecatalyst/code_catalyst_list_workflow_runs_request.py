from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .code_catalyst_workflow_run_sort_criteria import CodeCatalystWorkflowRunSortCriteria


class CodeCatalystListWorkflowRunsRequest(BaseModel):
    spaceName: StrictStr
    projectName: StrictStr
    workflowId: StrictStr | None = None
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    sortBy: list[CodeCatalystWorkflowRunSortCriteria] | None = None
