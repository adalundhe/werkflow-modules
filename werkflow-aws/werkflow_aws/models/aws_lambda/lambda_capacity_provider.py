from __future__ import annotations
from pydantic import BaseModel, StrictStr
from .lambda_capacity_provider_permissions_config import LambdaCapacityProviderPermissionsConfig
from .lambda_capacity_provider_scaling_config import LambdaCapacityProviderScalingConfig
from .lambda_capacity_provider_telemetry_config import LambdaCapacityProviderTelemetryConfig
from .lambda_capacity_provider_vpc_config import LambdaCapacityProviderVpcConfig
from .lambda_instance_requirements import LambdaInstanceRequirements
from .lambda_propagate_tags import LambdaPropagateTags


class LambdaCapacityProvider(BaseModel):
    CapacityProviderArn: StrictStr | None = None
    State: StrictStr | None = None
    VpcConfig: LambdaCapacityProviderVpcConfig | None = None
    PermissionsConfig: LambdaCapacityProviderPermissionsConfig | None = None
    InstanceRequirements: LambdaInstanceRequirements | None = None
    CapacityProviderScalingConfig: LambdaCapacityProviderScalingConfig | None = None
    KmsKeyArn: StrictStr | None = None
    LastModified: StrictStr | None = None
    PropagateTags: LambdaPropagateTags | None = None
    TelemetryConfig: LambdaCapacityProviderTelemetryConfig | None = None
