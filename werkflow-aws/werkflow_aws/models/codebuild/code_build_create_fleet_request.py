from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictInt, StrictStr
from .code_build_compute_configuration import CodeBuildComputeConfiguration
from .code_build_proxy_configuration import CodeBuildProxyConfiguration
from .code_build_scaling_configuration_input import CodeBuildScalingConfigurationInput
from .code_build_tag import CodeBuildTag
from .code_build_vpc_config import CodeBuildVpcConfig


class CodeBuildCreateFleetRequest(BaseModel):
    name: StrictStr
    baseCapacity: StrictInt
    environmentType: Literal['WINDOWS_CONTAINER', 'LINUX_CONTAINER', 'LINUX_GPU_CONTAINER', 'ARM_CONTAINER', 'WINDOWS_SERVER_2019_CONTAINER', 'WINDOWS_SERVER_2022_CONTAINER', 'LINUX_LAMBDA_CONTAINER', 'ARM_LAMBDA_CONTAINER', 'LINUX_EC2', 'ARM_EC2', 'WINDOWS_EC2', 'MAC_ARM']
    computeType: Literal['BUILD_GENERAL1_SMALL', 'BUILD_GENERAL1_MEDIUM', 'BUILD_GENERAL1_LARGE', 'BUILD_GENERAL1_XLARGE', 'BUILD_GENERAL1_2XLARGE', 'BUILD_LAMBDA_1GB', 'BUILD_LAMBDA_2GB', 'BUILD_LAMBDA_4GB', 'BUILD_LAMBDA_8GB', 'BUILD_LAMBDA_10GB', 'ATTRIBUTE_BASED_COMPUTE', 'CUSTOM_INSTANCE_TYPE']
    computeConfiguration: CodeBuildComputeConfiguration | None = None
    scalingConfiguration: CodeBuildScalingConfigurationInput | None = None
    overflowBehavior: Literal['QUEUE', 'ON_DEMAND'] | None = None
    vpcConfig: CodeBuildVpcConfig | None = None
    proxyConfiguration: CodeBuildProxyConfiguration | None = None
    imageId: StrictStr | None = None
    fleetServiceRole: StrictStr | None = None
    tags: list[CodeBuildTag] | None = None
