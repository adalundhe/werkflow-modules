from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .code_catalyst_workflow_definition_summary import CodeCatalystWorkflowDefinitionSummary


class CodeCatalystWorkflowSummary(BaseModel):
    id: StrictStr | None = None
    name: StrictStr | None = None
    sourceRepositoryName: StrictStr | None = None
    sourceBranchName: StrictStr | None = None
    definition: CodeCatalystWorkflowDefinitionSummary | None = None
    createdTime: datetime.datetime | StrictStr | None = None
    lastUpdatedTime: datetime.datetime | StrictStr | None = None
    runMode: StrictStr | None = None
    status: StrictStr | None = None
