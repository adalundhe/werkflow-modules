from __future__ import annotations
from typing import Literal
from pydantic import BaseModel, StrictBool, StrictStr
from .app_stream_agent_access_setting import AppStreamAgentAccessSetting


class AppStreamImageBuilderAgentAccessConfigForUpdate(BaseModel):
    Settings: list[AppStreamAgentAccessSetting] | None = None
    S3BucketArn: StrictStr | None = None
    ScreenshotsUploadEnabled: StrictBool | None = None
    ScreenResolution: Literal['W_1280xH_720'] | None = None
    ScreenImageFormat: Literal['PNG', 'JPEG'] | None = None
    UserControlMode: Literal['VIEW_ONLY', 'VIEW_STOP', 'DISABLED'] | None = None
