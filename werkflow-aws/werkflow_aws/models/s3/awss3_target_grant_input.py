from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .awss3_grantee_input import AWSS3GranteeInput


class AWSS3TargetGrantInput(BaseModel):
    Grantee: AWSS3GranteeInput | None = None
    Permission: Literal['FULL_CONTROL', 'READ', 'WRITE'] | None = None
