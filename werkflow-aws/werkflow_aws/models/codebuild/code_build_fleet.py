from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictInt, StrictStr
from .code_build_compute_configuration import CodeBuildComputeConfiguration
from .code_build_fleet_status import CodeBuildFleetStatus
from .code_build_proxy_configuration import CodeBuildProxyConfiguration
from .code_build_scaling_configuration_output import CodeBuildScalingConfigurationOutput
from .code_build_tag import CodeBuildTag
from .code_build_vpc_config import CodeBuildVpcConfig


class CodeBuildFleet(BaseModel):
    arn: StrictStr | None = None
    name: StrictStr | None = None
    id: StrictStr | None = None
    created: datetime.datetime | StrictStr | None = None
    lastModified: datetime.datetime | StrictStr | None = None
    status: CodeBuildFleetStatus | None = None
    baseCapacity: StrictInt | None = None
    environmentType: StrictStr | None = None
    computeType: StrictStr | None = None
    computeConfiguration: CodeBuildComputeConfiguration | None = None
    scalingConfiguration: CodeBuildScalingConfigurationOutput | None = None
    overflowBehavior: StrictStr | None = None
    vpcConfig: CodeBuildVpcConfig | None = None
    proxyConfiguration: CodeBuildProxyConfiguration | None = None
    imageId: StrictStr | None = None
    fleetServiceRole: StrictStr | None = None
    tags: list[CodeBuildTag] | None = None
