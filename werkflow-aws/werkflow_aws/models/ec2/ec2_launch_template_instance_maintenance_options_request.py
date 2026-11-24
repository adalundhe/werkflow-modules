from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class EC2LaunchTemplateInstanceMaintenanceOptionsRequest(BaseModel):
    AutoRecovery: Literal['default', 'disabled'] | None = None
