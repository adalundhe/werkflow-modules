from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_create_resource_identifier import ProjectCreateResourceIdentifier
from .workflow_status_layout_payload import WorkflowStatusLayoutPayload


class WorkflowStatusPayload(BaseModel):
    layout: WorkflowStatusLayoutPayload | None = None
    pcri: ProjectCreateResourceIdentifier | None = None
    properties: dict[StrictStr, StrictStr] | None = None
