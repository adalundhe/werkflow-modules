from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .app_stream_s3_location import AppStreamS3Location


class AppStreamUpdateApplicationRequest(BaseModel):
    Name: StrictStr
    DisplayName: StrictStr | None = None
    Description: StrictStr | None = None
    IconS3Location: AppStreamS3Location | None = None
    LaunchPath: StrictStr | None = None
    WorkingDirectory: StrictStr | None = None
    LaunchParameters: StrictStr | None = None
    AppBlockArn: StrictStr | None = None
    AttributesToDelete: list[Literal['LAUNCH_PARAMETERS', 'WORKING_DIRECTORY']] | None = None
