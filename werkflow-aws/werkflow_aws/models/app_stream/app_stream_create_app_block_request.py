from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictStr
from .app_stream_s3_location import AppStreamS3Location
from .app_stream_script_details import AppStreamScriptDetails


class AppStreamCreateAppBlockRequest(BaseModel):
    Name: StrictStr
    SourceS3Location: AppStreamS3Location
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    SetupScriptDetails: AppStreamScriptDetails | None = None
    Tags: dict[StrictStr, StrictStr] | None = None
    PostSetupScriptDetails: AppStreamScriptDetails | None = None
    PackagingType: Literal['CUSTOM', 'APPSTREAM2'] | None = None
