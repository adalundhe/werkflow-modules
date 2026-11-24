from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .project_details import ProjectDetails
from .published_workflow_id import PublishedWorkflowId
from .transition import Transition
from .workflow_operations import WorkflowOperations
from .workflow_scheme_id_name import WorkflowSchemeIdName
from .workflow_status import WorkflowStatus


class Workflow(BaseModel):
    created: StrictStr | None = None
    description: StrictStr | None = None
    hasDraftWorkflow: StrictBool | None = None
    id: PublishedWorkflowId | None = None
    isDefault: StrictBool | None = None
    operations: WorkflowOperations | None = None
    projects: list[ProjectDetails] | None = None
    schemes: list[WorkflowSchemeIdName] | None = None
    statuses: list[WorkflowStatus] | None = None
    transitions: list[Transition] | None = None
    updated: StrictStr | None = None
