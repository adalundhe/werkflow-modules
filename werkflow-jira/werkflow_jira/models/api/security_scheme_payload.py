from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .project_create_resource_identifier import ProjectCreateResourceIdentifier
from .security_level_payload import SecurityLevelPayload


class SecuritySchemePayload(BaseModel):
    description: StrictStr | None = None
    name: StrictStr | None = None
    pcri: ProjectCreateResourceIdentifier | None = None
    securityLevels: list[SecurityLevelPayload] | None = None
