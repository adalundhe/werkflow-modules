from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EKSBlockStorageModel(BaseModel):
    enabled: StrictBool | None = None
