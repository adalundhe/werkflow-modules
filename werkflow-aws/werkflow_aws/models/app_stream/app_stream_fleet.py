from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictInt, StrictStr
from .app_stream_compute_capacity_status import AppStreamComputeCapacityStatus
from .app_stream_domain_join_info import AppStreamDomainJoinInfo
from .app_stream_fleet_error import AppStreamFleetError
from .app_stream_s3_location import AppStreamS3Location
from .app_stream_volume_config import AppStreamVolumeConfig
from .app_stream_vpc_config import AppStreamVpcConfig


class AppStreamFleet(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    DisplayName: StrictStr | None = None
    Description: StrictStr | None = None
    ImageName: StrictStr | None = None
    ImageArn: StrictStr | None = None
    InstanceType: StrictStr | None = None
    FleetType: StrictStr | None = None
    ComputeCapacityStatus: AppStreamComputeCapacityStatus | None = None
    MaxUserDurationInSeconds: StrictInt | None = None
    DisconnectTimeoutInSeconds: StrictInt | None = None
    State: StrictStr | None = None
    VpcConfig: AppStreamVpcConfig | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    FleetErrors: list[AppStreamFleetError] | None = None
    EnableDefaultInternetAccess: StrictBool | None = None
    DomainJoinInfo: AppStreamDomainJoinInfo | None = None
    IdleDisconnectTimeoutInSeconds: StrictInt | None = None
    IamRoleArn: StrictStr | None = None
    StreamView: StrictStr | None = None
    Platform: StrictStr | None = None
    MaxConcurrentSessions: StrictInt | None = None
    UsbDeviceFilterStrings: list[StrictStr] | None = None
    SessionScriptS3Location: AppStreamS3Location | None = None
    MaxSessionsPerInstance: StrictInt | None = None
    RootVolumeConfig: AppStreamVolumeConfig | None = None
    DisableIMDSV1: StrictBool | None = None
