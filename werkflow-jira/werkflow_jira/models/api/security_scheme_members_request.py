from __future__ import annotations
from pydantic import BaseModel
from .security_scheme_level_member_bean import SecuritySchemeLevelMemberBean


class SecuritySchemeMembersRequest(BaseModel):
    members: list[SecuritySchemeLevelMemberBean] | None = None
