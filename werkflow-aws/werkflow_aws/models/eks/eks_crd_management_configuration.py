from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EKSCrdManagementConfiguration(BaseModel):
    managed: StrictBool | None = None
