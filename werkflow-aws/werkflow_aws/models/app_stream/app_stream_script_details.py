from __future__ import annotations
from pydantic import BaseModel, StrictInt, StrictStr
from .app_stream_s3_location import AppStreamS3Location


class AppStreamScriptDetails(BaseModel):
    ScriptS3Location: AppStreamS3Location | None = None
    ExecutablePath: StrictStr | None = None
    ExecutableParameters: StrictStr | None = None
    TimeoutInSeconds: StrictInt | None = None
