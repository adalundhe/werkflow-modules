from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .document_version import DocumentVersion
from .workflow_metadata_and_issue_type_rest_model import WorkflowMetadataAndIssueTypeRestModel
from .workflow_metadata_rest_model import WorkflowMetadataRestModel
from .workflow_scope import WorkflowScope


class WorkflowSchemeReadResponse(BaseModel):
    defaultWorkflow: WorkflowMetadataRestModel | None = None
    description: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    scope: WorkflowScope | None = None
    taskId: StrictStr | None = None
    version: DocumentVersion | None = None
    workflowsForIssueTypes: list[WorkflowMetadataAndIssueTypeRestModel] | None = None
