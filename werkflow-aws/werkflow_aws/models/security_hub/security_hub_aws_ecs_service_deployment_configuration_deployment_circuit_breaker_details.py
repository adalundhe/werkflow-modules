from __future__ import annotations
from pydantic import BaseModel, StrictBool


class SecurityHubAwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails(BaseModel):
    Enable: StrictBool | None = None
    Rollback: StrictBool | None = None
