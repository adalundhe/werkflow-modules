from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr


class VerifiedPermissionsDeletePolicyStoreAliasRequest(BaseModel):
    aliasName: StrictStr
    deletionMode: Literal['SoftDelete', 'HardDelete'] | None = None
