from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .workflow_preview_scope import WorkflowPreviewScope


class JiraWorkflowPreviewStatus(BaseModel):
    description: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    rawName: StrictStr | None = None
    scope: WorkflowPreviewScope | None = None
    statusCategory: StrictStr | None = None
    statusReference: StrictStr | None = None
