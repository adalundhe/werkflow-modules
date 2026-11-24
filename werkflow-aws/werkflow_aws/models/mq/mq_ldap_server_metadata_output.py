from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MQLdapServerMetadataOutput(BaseModel):
    Hosts: list[StrictStr] | None = None
    RoleBase: StrictStr | None = None
    RoleName: StrictStr | None = None
    RoleSearchMatching: StrictStr | None = None
    RoleSearchSubtree: StrictBool | None = None
    ServiceAccountUsername: StrictStr | None = None
    UserBase: StrictStr | None = None
    UserRoleName: StrictStr | None = None
    UserSearchMatching: StrictStr | None = None
    UserSearchSubtree: StrictBool | None = None
