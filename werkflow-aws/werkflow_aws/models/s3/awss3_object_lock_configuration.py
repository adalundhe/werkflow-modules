from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .awss3_object_lock_rule import AWSS3ObjectLockRule


class AWSS3ObjectLockConfiguration(BaseModel):
    ObjectLockEnabled: Literal['Enabled'] | None = None
    Rule: AWSS3ObjectLockRule | None = None
