from __future__ import annotations
from pydantic import BaseModel
from .awss3_default_retention_input import AWSS3DefaultRetentionInput


class AWSS3ObjectLockRuleInput(BaseModel):
    DefaultRetention: AWSS3DefaultRetentionInput | None = None
