from __future__ import annotations
from typing import Literal
from pydantic import BaseModel


class Route53GetAccountLimitRequest(BaseModel):
    Type: Literal['MAX_HEALTH_CHECKS_BY_OWNER', 'MAX_HOSTED_ZONES_BY_OWNER', 'MAX_TRAFFIC_POLICY_INSTANCES_BY_OWNER', 'MAX_REUSABLE_DELEGATION_SETS_BY_OWNER', 'MAX_TRAFFIC_POLICIES_BY_OWNER', 'MAX_HEALTH_CHECK_SOURCES_BY_OWNER']
