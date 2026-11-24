from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class GuardDutyOrganizationAdditionalConfiguration(BaseModel):
    Name: Literal['EKS_ADDON_MANAGEMENT', 'ECS_FARGATE_AGENT_MANAGEMENT', 'EC2_AGENT_MANAGEMENT', 'RDS_DATA_RISK'] | None = None
    AutoEnable: Literal['NEW', 'NONE', 'ALL'] | None = None
