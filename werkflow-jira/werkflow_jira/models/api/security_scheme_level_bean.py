from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .security_scheme_level_member_bean import SecuritySchemeLevelMemberBean


class SecuritySchemeLevelBean(BaseModel):
    description: StrictStr | None = None
    isDefault: StrictBool | None = None
    members: list[SecuritySchemeLevelMemberBean] | None = None
    name: StrictStr | None = None
