from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .code_catalyst_workflow_sort_criteria import CodeCatalystWorkflowSortCriteria


class CodeCatalystListWorkflowsRequest(BaseModel):
    spaceName: StrictStr
    projectName: StrictStr
    nextToken: StrictStr | None = None
    maxResults: StrictInt | None = None
    sortBy: list[CodeCatalystWorkflowSortCriteria] | None = None
