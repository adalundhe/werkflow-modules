from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .awss3_grantee_input import AWSS3GranteeInput


class AWSS3GrantInput(BaseModel):
    Grantee: AWSS3GranteeInput | None = None
    Permission: Literal['FULL_CONTROL', 'WRITE', 'WRITE_ACP', 'READ', 'READ_ACP'] | None = None
