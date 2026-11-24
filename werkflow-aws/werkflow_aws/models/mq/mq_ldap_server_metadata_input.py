from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class MQLdapServerMetadataInput(BaseModel):
    Hosts: list[StrictStr]
    RoleBase: StrictStr
    RoleSearchMatching: StrictStr
    ServiceAccountPassword: StrictStr
    ServiceAccountUsername: StrictStr
    UserBase: StrictStr
    UserSearchMatching: StrictStr
    RoleName: StrictStr | None = None
    RoleSearchSubtree: StrictBool | None = None
    UserRoleName: StrictStr | None = None
    UserSearchSubtree: StrictBool | None = None
