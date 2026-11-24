from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .app_stream_access_endpoint import AppStreamAccessEndpoint
from .app_stream_domain_join_info import AppStreamDomainJoinInfo
from .app_stream_image_builder_agent_access_config import AppStreamImageBuilderAgentAccessConfig
from .app_stream_image_builder_state_change_reason import AppStreamImageBuilderStateChangeReason
from .app_stream_network_access_configuration import AppStreamNetworkAccessConfiguration
from .app_stream_resource_error import AppStreamResourceError
from .app_stream_volume_config import AppStreamVolumeConfig
from .app_stream_vpc_config import AppStreamVpcConfig


class AppStreamImageBuilder(BaseModel):
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    ImageArn: StrictStr | None = None
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    VpcConfig: AppStreamVpcConfig | None = None
    InstanceType: StrictStr | None = None
    Platform: StrictStr | None = None
    IamRoleArn: StrictStr | None = None
    State: StrictStr | None = None
    StateChangeReason: AppStreamImageBuilderStateChangeReason | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    EnableDefaultInternetAccess: StrictBool | None = None
    DomainJoinInfo: AppStreamDomainJoinInfo | None = None
    NetworkAccessConfiguration: AppStreamNetworkAccessConfiguration | None = None
    ImageBuilderErrors: list[AppStreamResourceError] | None = None
    AppstreamAgentVersion: StrictStr | None = None
    AccessEndpoints: list[AppStreamAccessEndpoint] | None = None
    RootVolumeConfig: AppStreamVolumeConfig | None = None
    LatestAppstreamAgentVersion: StrictStr | None = None
    DisableIMDSV1: StrictBool | None = None
    AgentAccessConfig: AppStreamImageBuilderAgentAccessConfig | None = None
