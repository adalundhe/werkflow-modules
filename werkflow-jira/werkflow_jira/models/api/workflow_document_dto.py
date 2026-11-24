from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .document_version import DocumentVersion
from .workflow_layout import WorkflowLayout
from .workflow_reference_status import WorkflowReferenceStatus
from .workflow_scope import WorkflowScope
from .workflow_transitions import WorkflowTransitions


class WorkflowDocumentDTO(BaseModel):
    created: StrictStr | None = None
    description: StrictStr | None = None
    id: StrictStr | None = None
    lastUpdateAuthorAAID: StrictStr | None = None
    loopedTransitionContainerLayout: WorkflowLayout | None = None
    name: StrictStr | None = None
    scope: WorkflowScope | None = None
    startPointLayout: WorkflowLayout | None = None
    statuses: list[WorkflowReferenceStatus] | None = None
    transitions: list[WorkflowTransitions] | None = None
    updated: StrictStr | None = None
    version: DocumentVersion | None = None
