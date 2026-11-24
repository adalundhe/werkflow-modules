from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .app_stream_access_endpoint import AppStreamAccessEndpoint
from .app_stream_vpc_config import AppStreamVpcConfig


class AppStreamCreateAppBlockBuilderRequest(BaseModel):
    Name: StrictStr
    Platform: Literal['WINDOWS_SERVER_2019']
    InstanceType: StrictStr
    VpcConfig: AppStreamVpcConfig
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    EnableDefaultInternetAccess: StrictBool | None = None
    IamRoleArn: StrictStr | None = None
    AccessEndpoints: list[AppStreamAccessEndpoint] | None = None
    DisableIMDSV1: StrictBool | None = None
