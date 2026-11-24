from __future__ import annotations
from pydantic import BaseModel
from .awss3_rule import AWSS3Rule


class AWSS3LifecycleConfiguration(BaseModel):
    Rules: list[AWSS3Rule]
