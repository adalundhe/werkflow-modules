from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .workflow_scheme_association import WorkflowSchemeAssociation


class WorkflowSchemeUpdateRequiredMappingsRequest(BaseModel):
    defaultWorkflowId: StrictStr | None = None
    id: StrictStr | None = None
    workflowsForIssueTypes: list[WorkflowSchemeAssociation] | None = None
