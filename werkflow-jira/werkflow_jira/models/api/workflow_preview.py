from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_issue_type_query_context import ProjectIssueTypeQueryContext
from .transition_preview import TransitionPreview
from .workflow_document_version_bean import WorkflowDocumentVersionBean
from .workflow_preview_layout import WorkflowPreviewLayout
from .workflow_preview_scope import WorkflowPreviewScope
from .workflow_preview_status import WorkflowPreviewStatus


class WorkflowPreview(BaseModel):
    description: StrictStr | None = None
    id: StrictStr | None = None
    loopedTransitionContainerLayout: WorkflowPreviewLayout | None = None
    name: StrictStr | None = None
    queryContext: list[ProjectIssueTypeQueryContext] | None = None
    scope: WorkflowPreviewScope | None = None
    startPointLayout: WorkflowPreviewLayout | None = None
    statuses: list[WorkflowPreviewStatus] | None = None
    transitions: list[TransitionPreview] | None = None
    version: WorkflowDocumentVersionBean | None = None
