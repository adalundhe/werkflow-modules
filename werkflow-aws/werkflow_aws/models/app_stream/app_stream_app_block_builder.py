from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .app_stream_access_endpoint import AppStreamAccessEndpoint
from .app_stream_app_block_builder_state_change_reason import AppStreamAppBlockBuilderStateChangeReason
from .app_stream_resource_error import AppStreamResourceError
from .app_stream_vpc_config import AppStreamVpcConfig


class AppStreamAppBlockBuilder(BaseModel):
    Arn: StrictStr | None = None
    Name: StrictStr | None = None
    DisplayName: StrictStr | None = None
    Description: StrictStr | None = None
    Platform: StrictStr | None = None
    InstanceType: StrictStr | None = None
    EnableDefaultInternetAccess: StrictBool | None = None
    IamRoleArn: StrictStr | None = None
    VpcConfig: AppStreamVpcConfig | None = None
    State: StrictStr | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    AppBlockBuilderErrors: list[AppStreamResourceError] | None = None
    StateChangeReason: AppStreamAppBlockBuilderStateChangeReason | None = None
    AccessEndpoints: list[AppStreamAccessEndpoint] | None = None
    DisableIMDSV1: StrictBool | None = None
