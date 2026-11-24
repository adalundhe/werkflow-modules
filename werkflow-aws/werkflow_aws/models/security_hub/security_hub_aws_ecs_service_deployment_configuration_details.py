from __future__ import annotations
from pydantic import BaseModel, StrictInt
from .security_hub_aws_ecs_service_deployment_configuration_deployment_circuit_breaker_details import SecurityHubAwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails


class SecurityHubAwsEcsServiceDeploymentConfigurationDetails(BaseModel):
    DeploymentCircuitBreaker: SecurityHubAwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails | None = None
    MaximumPercent: StrictInt | None = None
    MinimumHealthyPercent: StrictInt | None = None
