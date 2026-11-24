from __future__ import annotations
from pydantic import BaseModel, StrictBool


class AWSS3PolicyStatus(BaseModel):
    IsPublic: StrictBool | None = None
