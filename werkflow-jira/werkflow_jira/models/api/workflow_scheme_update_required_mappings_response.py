from __future__ import annotations
from pydantic import BaseModel
from .required_mapping_by_issue_type import RequiredMappingByIssueType
from .required_mapping_by_workflows import RequiredMappingByWorkflows
from .status_metadata import StatusMetadata
from .statuses_per_workflow import StatusesPerWorkflow


class WorkflowSchemeUpdateRequiredMappingsResponse(BaseModel):
    statusMappingsByIssueTypes: list[RequiredMappingByIssueType] | None = None
    statusMappingsByWorkflows: list[RequiredMappingByWorkflows] | None = None
    statuses: list[StatusMetadata] | None = None
    statusesPerWorkflow: list[StatusesPerWorkflow] | None = None
