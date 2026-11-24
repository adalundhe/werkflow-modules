from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .project_create_resource_identifier import ProjectCreateResourceIdentifier
from .security_level_member_payload import SecurityLevelMemberPayload


class SecurityLevelPayload(BaseModel):
    description: StrictStr | None = None
    isDefault: StrictBool | None = None
    name: StrictStr | None = None
    pcri: ProjectCreateResourceIdentifier | None = None
    securityLevelMembers: list[SecurityLevelMemberPayload] | None = None
