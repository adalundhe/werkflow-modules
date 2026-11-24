from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr
from .app_stream_agent_access_setting import AppStreamAgentAccessSetting


class AppStreamImageBuilderAgentAccessConfig(BaseModel):
    Settings: list[AppStreamAgentAccessSetting] | None = None
    S3BucketArn: StrictStr | None = None
    ScreenshotsUploadEnabled: StrictBool | None = None
    ScreenResolution: StrictStr | None = None
    ScreenImageFormat: StrictStr | None = None
    UserControlMode: StrictStr | None = None
