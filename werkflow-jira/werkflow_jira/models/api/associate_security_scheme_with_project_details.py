from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .old_to_new_security_level_mappings_bean import OldToNewSecurityLevelMappingsBean


class AssociateSecuritySchemeWithProjectDetails(BaseModel):
    oldToNewSecurityLevelMappings: list[OldToNewSecurityLevelMappingsBean] | None = None
    projectId: StrictStr | None = None
    schemeId: StrictStr | None = None
