from __future__ import annotations
from pydantic import BaseModel, StrictBool, StrictStr


class AppStreamApplicationSettingsResponse(BaseModel):
    Enabled: StrictBool | None = None
    SettingsGroup: StrictStr | None = None
    S3BucketName: StrictStr | None = None
