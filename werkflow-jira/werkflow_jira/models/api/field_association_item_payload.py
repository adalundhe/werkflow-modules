from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .project_create_resource_identifier import ProjectCreateResourceIdentifier


class FieldAssociationItemPayload(BaseModel):
    description: StrictStr | None = None
    pcri: ProjectCreateResourceIdentifier | None = None
    qualifierId: ProjectCreateResourceIdentifier | None = None
    qualifierType: ProjectCreateResourceIdentifier | None = None
    rendererType: StrictStr | None = None
    required: StrictBool | None = None
