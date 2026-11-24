from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_create_resource_identifier import ProjectCreateResourceIdentifier


class WorkflowSchemePayload(BaseModel):
    defaultWorkflow: ProjectCreateResourceIdentifier | None = None
    description: StrictStr | None = None
    explicitMappings: dict[StrictStr, ProjectCreateResourceIdentifier] | None = None
    name: StrictStr | None = None
    onConflict: StrictStr | None = None
    pcri: ProjectCreateResourceIdentifier | None = None
