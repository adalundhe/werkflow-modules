from __future__ import annotations
from typing import Literal
from pydantic import BaseModel
from .guard_duty_coverage_filter_condition import GuardDutyCoverageFilterCondition


class GuardDutyCoverageFilterCriterion(BaseModel):
    CriterionKey: Literal['ACCOUNT_ID', 'RESOURCE_TYPE', 'COVERAGE_STATUS', 'ADDON_VERSION', 'CLUSTER_NAME', 'ECS_CLUSTER_NAME', 'MANAGEMENT_TYPE', 'EKS_CLUSTER_NAME', 'AGENT_VERSION', 'INSTANCE_ID', 'CLUSTER_ARN'] | None = None
    FilterCondition: GuardDutyCoverageFilterCondition | None = None
