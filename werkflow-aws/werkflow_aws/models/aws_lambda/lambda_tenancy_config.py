from __future__ import annotations
from pydantic import BaseModel
from .lambda_tenant_isolation_mode import LambdaTenantIsolationMode


class LambdaTenancyConfig(BaseModel):
    TenantIsolationMode: LambdaTenantIsolationMode
