from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class GuardDutyMemberAdditionalConfiguration(BaseModel):
    Name: Literal['EKS_ADDON_MANAGEMENT', 'ECS_FARGATE_AGENT_MANAGEMENT', 'EC2_AGENT_MANAGEMENT', 'RDS_DATA_RISK'] | None = None
    Status: Literal['ENABLED', 'DISABLED'] | None = None
