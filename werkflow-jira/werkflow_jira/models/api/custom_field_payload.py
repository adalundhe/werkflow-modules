from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_create_resource_identifier import ProjectCreateResourceIdentifier


class CustomFieldPayload(BaseModel):
    cfType: StrictStr | None = None
    description: StrictStr | None = None
    name: StrictStr | None = None
    onConflict: StrictStr | None = None
    pcri: ProjectCreateResourceIdentifier | None = None
    scope: StrictStr | None = None
    searcherKey: StrictStr | None = None
