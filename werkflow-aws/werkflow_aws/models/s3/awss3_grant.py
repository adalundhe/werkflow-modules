from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .awss3_grantee import AWSS3Grantee


class AWSS3Grant(BaseModel):
    Grantee: AWSS3Grantee | None = None
    Permission: Literal['FULL_CONTROL', 'WRITE', 'WRITE_ACP', 'READ', 'READ_ACP'] | None = None
