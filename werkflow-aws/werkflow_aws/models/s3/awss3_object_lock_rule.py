from __future__ import annotations
from pydantic import BaseModel
from .awss3_default_retention import AWSS3DefaultRetention


class AWSS3ObjectLockRule(BaseModel):
    DefaultRetention: AWSS3DefaultRetention | None = None
