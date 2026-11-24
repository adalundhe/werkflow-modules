from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr


class OpenSearchIdentityCenterOptionsInput(BaseModel):
    EnabledAPIAccess: StrictBool | None = None
    IdentityCenterInstanceARN: StrictStr | None = None
    IdentityCenterInstanceRegion: StrictStr | None = None
    SubjectKey: Literal['UserName', 'UserId', 'Email'] | None = None
    RolesKey: Literal['GroupName', 'GroupId'] | None = None
