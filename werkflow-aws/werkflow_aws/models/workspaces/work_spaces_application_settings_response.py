from __future__ import annotations
from pydantic import BaseModel, StrictStr


class WorkSpacesApplicationSettingsResponse(BaseModel):
    Status: StrictStr | None = None
    SettingsGroup: StrictStr | None = None
    S3BucketName: StrictStr | None = None
