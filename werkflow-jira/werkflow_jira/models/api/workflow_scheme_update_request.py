from __future__ import annotations
from pydantic import BaseModel, ConfigDict, StrictStr
from .document_version import DocumentVersion
from .mappings_by_issue_type_override import MappingsByIssueTypeOverride
from .mappings_by_workflow import MappingsByWorkflow
from .workflow_scheme_association import WorkflowSchemeAssociation


class WorkflowSchemeUpdateRequest(BaseModel):
    model_config = ConfigDict(extra="allow")

    defaultWorkflowId: StrictStr | None = None
    description: StrictStr | None = None
    id: StrictStr | None = None
    name: StrictStr | None = None
    statusMappingsByIssueTypeOverride: list[MappingsByIssueTypeOverride] | None = None
    statusMappingsByWorkflows: list[MappingsByWorkflow] | None = None
    version: DocumentVersion | None = None
    workflowsForIssueTypes: list[WorkflowSchemeAssociation] | None = None
