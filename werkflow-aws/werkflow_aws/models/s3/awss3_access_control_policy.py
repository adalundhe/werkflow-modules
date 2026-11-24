from __future__ import annotations
from pydantic import BaseModel
from .awss3_grant_input import AWSS3GrantInput
from .awss3_owner_input import AWSS3OwnerInput


class AWSS3AccessControlPolicy(BaseModel):
    Grants: list[AWSS3GrantInput] | None = None
    Owner: AWSS3OwnerInput | None = None
