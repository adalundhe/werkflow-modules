from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .app_stream_access_endpoint import AppStreamAccessEndpoint
from .app_stream_domain_join_info import AppStreamDomainJoinInfo
from .app_stream_image_builder_agent_access_config import AppStreamImageBuilderAgentAccessConfig
from .app_stream_volume_config import AppStreamVolumeConfig
from .app_stream_vpc_config import AppStreamVpcConfig


class AppStreamCreateImageBuilderRequest(BaseModel):
    Name: StrictStr
    InstanceType: StrictStr
    ImageName: StrictStr | None = None
    ImageArn: StrictStr | None = None
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    VpcConfig: AppStreamVpcConfig | None = None
    IamRoleArn: StrictStr | None = None
    EnableDefaultInternetAccess: StrictBool | None = None
    DomainJoinInfo: AppStreamDomainJoinInfo | None = None
    AppstreamAgentVersion: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    AccessEndpoints: list[AppStreamAccessEndpoint] | None = None
    RootVolumeConfig: AppStreamVolumeConfig | None = None
    SoftwaresToInstall: list[StrictStr] | None = None
    SoftwaresToUninstall: list[StrictStr] | None = None
    DisableIMDSV1: StrictBool | None = None
    AgentAccessConfig: AppStreamImageBuilderAgentAccessConfig | None = None
