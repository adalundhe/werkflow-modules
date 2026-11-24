from __future__ import annotations
from pydantic import BaseModel, StrictBool


class EKSCrdManagementConfigurationModel(BaseModel):
    managed: StrictBool | None = None
