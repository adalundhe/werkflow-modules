from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .app_stream_access_endpoint import AppStreamAccessEndpoint
from .app_stream_vpc_config import AppStreamVpcConfig


class AppStreamUpdateAppBlockBuilderRequest(BaseModel):
    Name: StrictStr
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    Platform: Literal['WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022', 'WINDOWS_SERVER_2025', 'WINDOWS_11', 'AMAZON_LINUX2', 'RHEL8', 'ROCKY_LINUX8', 'UBUNTU_PRO_2404'] | None = None
    InstanceType: StrictStr | None = None
    VpcConfig: AppStreamVpcConfig | None = None
    EnableDefaultInternetAccess: StrictBool | None = None
    IamRoleArn: StrictStr | None = None
    AccessEndpoints: list[AppStreamAccessEndpoint] | None = None
    AttributesToDelete: list[Literal['IAM_ROLE_ARN', 'ACCESS_ENDPOINTS', 'VPC_CONFIGURATION_SECURITY_GROUP_IDS']] | None = None
    DisableIMDSV1: StrictBool | None = None
