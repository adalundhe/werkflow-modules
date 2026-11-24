from __future__ import annotations
import datetime
from pydantic import BaseModel, StrictStr
from .app_stream_error_details import AppStreamErrorDetails
from .app_stream_s3_location import AppStreamS3Location
from .app_stream_script_details import AppStreamScriptDetails


class AppStreamAppBlock(BaseModel):
    Name: StrictStr | None = None
    Arn: StrictStr | None = None
    Description: StrictStr | None = None
    DisplayName: StrictStr | None = None
    SourceS3Location: AppStreamS3Location | None = None
    SetupScriptDetails: AppStreamScriptDetails | None = None
    CreatedTime: datetime.datetime | StrictStr | None = None
    PostSetupScriptDetails: AppStreamScriptDetails | None = None
    PackagingType: StrictStr | None = None
    State: StrictStr | None = None
    AppBlockErrors: list[AppStreamErrorDetails] | None = None
