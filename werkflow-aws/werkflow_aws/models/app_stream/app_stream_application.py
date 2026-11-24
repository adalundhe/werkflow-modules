from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictBool, StrictStr
from .app_stream_s3_location import AppStreamS3Location


class AppStreamApplication(BaseModel):
    Name: StrictStr | None = None
    DisplayName: StrictStr | None = None
    IconURL: StrictStr | None = None
    LaunchPath: StrictStr | None = None
    LaunchParameters: StrictStr | None = None
    Enabled: StrictBool | None = None
    Metadata: dict[StrictStr, StrictStr] | None = None
    WorkingDirectory: StrictStr | None = None
    Description: StrictStr | None = None
    Arn: StrictStr | None = None
    AppBlockArn: StrictStr | None = None
    IconS3Location: AppStreamS3Location | None = None
    Platforms: list[StrictStr] | None = None
    InstanceFamilies: list[StrictStr] | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
