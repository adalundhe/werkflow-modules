from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EKSBlockStorage(BaseModel):
    enabled: StrictBool | None = None
