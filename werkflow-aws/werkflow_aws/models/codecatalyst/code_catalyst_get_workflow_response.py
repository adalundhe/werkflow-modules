from __future__ import annotations
import datetime
from typing import Any
from pydantic import BaseModel, StrictStr
from .code_catalyst_workflow_definition import CodeCatalystWorkflowDefinition


class CodeCatalystGetWorkflowResponse(BaseModel):
    spaceName: StrictStr | None = None
    projectName: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    sourceRepositoryName: StrictStr | None = None
    sourceBranchName: StrictStr | None = None
    definition: CodeCatalystWorkflowDefinition | None = None
    createdTime: datetime.datetime | StrictStr | None = None
    lastUpdatedTime: datetime.datetime | StrictStr | None = None
    runMode: StrictStr | None = None
    status: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
