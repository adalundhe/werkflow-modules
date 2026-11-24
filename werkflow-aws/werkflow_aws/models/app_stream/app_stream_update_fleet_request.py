from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .app_stream_compute_capacity import AppStreamComputeCapacity
from .app_stream_domain_join_info import AppStreamDomainJoinInfo
from .app_stream_s3_location import AppStreamS3Location
from .app_stream_volume_config import AppStreamVolumeConfig
from .app_stream_vpc_config import AppStreamVpcConfig


class AppStreamUpdateFleetRequest(BaseModel):
    ImageName: StrictStr | None = None
    ImageArn: StrictStr | None = None
    Name: StrictStr | None = None
    InstanceType: StrictStr | None = None
    ComputeCapacity: AppStreamComputeCapacity | None = None
    VpcConfig: AppStreamVpcConfig | None = None
    MaxUserDurationInSeconds: StrictInt | None = None
    DisconnectTimeoutInSeconds: StrictInt | None = None
    DeleteVpcConfig: StrictBool | None = None
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    EnableDefaultInternetAccess: StrictBool | None = None
    DomainJoinInfo: AppStreamDomainJoinInfo | None = None
    IdleDisconnectTimeoutInSeconds: StrictInt | None = None
    AttributesToDelete: list[Literal['VPC_CONFIGURATION', 'VPC_CONFIGURATION_SECURITY_GROUP_IDS', 'DOMAIN_JOIN_INFO', 'IAM_ROLE_ARN', 'USB_DEVICE_FILTER_STRINGS', 'SESSION_SCRIPT_S3_LOCATION', 'MAX_SESSIONS_PER_INSTANCE', 'VOLUME_CONFIGURATION']] | None = None
    IamRoleArn: StrictStr | None = None
    StreamView: Literal['APP', 'DESKTOP'] | None = None
    Platform: Literal['WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022', 'WINDOWS_SERVER_2025', 'WINDOWS_11', 'AMAZON_LINUX2', 'RHEL8', 'ROCKY_LINUX8', 'UBUNTU_PRO_2404'] | None = None
    MaxConcurrentSessions: StrictInt | None = None
    UsbDeviceFilterStrings: list[StrictStr] | None = None
    SessionScriptS3Location: AppStreamS3Location | None = None
    MaxSessionsPerInstance: StrictInt | None = None
    RootVolumeConfig: AppStreamVolumeConfig | None = None
    DisableIMDSV1: StrictBool | None = None
