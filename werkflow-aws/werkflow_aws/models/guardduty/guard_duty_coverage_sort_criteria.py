from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class GuardDutyCoverageSortCriteria(BaseModel):
    AttributeName: Literal['ACCOUNT_ID', 'COVERAGE_STATUS', 'ISSUE', 'ADDON_VERSION', 'UPDATED_AT', 'CLUSTER_NAME', 'EKS_CLUSTER_NAME', 'ECS_CLUSTER_NAME', 'INSTANCE_ID'] | None = None
    OrderBy: Literal['ASC', 'DESC'] | None = None
