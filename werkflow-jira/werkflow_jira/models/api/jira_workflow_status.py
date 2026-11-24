from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .workflow_scope import WorkflowScope


class JiraWorkflowStatus(BaseModel):
    description: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    scope: WorkflowScope | None = None
    statusCategory: StrictStr | None = None
    statusReference: StrictStr | None = None
