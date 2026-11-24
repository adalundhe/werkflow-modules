from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .app_stream_s3_location import AppStreamS3Location


class AppStreamCreateApplicationRequest(BaseModel):
    Name: StrictStr
    IconS3Location: AppStreamS3Location
    LaunchPath: StrictStr
    Platforms: list[Literal['WINDOWS', 'WINDOWS_SERVER_2016', 'WINDOWS_SERVER_2019', 'WINDOWS_SERVER_2022', 'WINDOWS_SERVER_2025', 'WINDOWS_11', 'AMAZON_LINUX2', 'RHEL8', 'ROCKY_LINUX8', 'UBUNTU_PRO_2404']]
    InstanceFamilies: list[StrictStr]
    AppBlockArn: StrictStr
    DisplayName: StrictStr | None = None
    Description: StrictStr | None = None
    WorkingDirectory: StrictStr | None = None
    LaunchParameters: StrictStr | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
