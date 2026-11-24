from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .document_version import DocumentVersion
from .workflow_layout import WorkflowLayout
from .workflow_reference_status import WorkflowReferenceStatus
from .workflow_scope import WorkflowScope
from .workflow_transitions import WorkflowTransitions


class JiraWorkflow(BaseModel):
    created: StrictStr | None = None
    description: StrictStr | None = None
    id: StrictStr | None = None
    isEditable: StrictBool | None = None
    loopedTransitionContainerLayout: WorkflowLayout | None = None
    name: StrictStr | None = None
    scope: WorkflowScope | None = None
    startPointLayout: WorkflowLayout | None = None
    statuses: list[WorkflowReferenceStatus] | None = None
    taskId: StrictStr | None = None
    transitions: list[WorkflowTransitions] | None = None
    updated: StrictStr | None = None
    version: DocumentVersion | None = None
