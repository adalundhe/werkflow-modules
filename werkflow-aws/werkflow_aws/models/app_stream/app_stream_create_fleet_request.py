from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .app_stream_compute_capacity import AppStreamComputeCapacity
from .app_stream_domain_join_info import AppStreamDomainJoinInfo
from .app_stream_s3_location import AppStreamS3Location
from .app_stream_volume_config import AppStreamVolumeConfig
from .app_stream_vpc_config import AppStreamVpcConfig


class AppStreamCreateFleetRequest(BaseModel):
    Name: StrictStr
    InstanceType: StrictStr
    ImageName: StrictStr | None = None
    ImageArn: StrictStr | None = None
    FleetType: Literal['ALWAYS_ON', 'ON_DEMAND', 'ELASTIC'] | None = None
    ComputeCapacity: AppStreamComputeCapacity | None = None
    VpcConfig: AppStreamVpcConfig | None = None
    MaxUserDurationInSeconds: StrictInt | None = None
    DisconnectTimeoutInSeconds: StrictInt | None = None
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    EnableDefaultInternetAccess: StrictBool | None = None
    DomainJoinInfo: AppStreamDomainJoinInfo | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    IdleDisconnectTimeoutInSeconds: StrictInt | None = None
    IamRoleArn: StrictStr | None = None
    StreamView: Literal['APP', 'DESKTOP'] | None = None
    Platform: Literal['WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022', 'WINDOWS_SERVER_2025', 'WINDOWS_11', 'AMAZON_LINUX2', 'RHEL8', 'ROCKY_LINUX8', 'UBUNTU_PRO_2404'] | None = None
    MaxConcurrentSessions: StrictInt | None = None
    UsbDeviceFilterStrings: list[StrictStr] | None = None
    SessionScriptS3Location: AppStreamS3Location | None = None
    MaxSessionsPerInstance: StrictInt | None = None
    RootVolumeConfig: AppStreamVolumeConfig | None = None
    DisableIMDSV1: StrictBool | None = None
