from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncAwsIamConfig(BaseModel):
    signingRegion: StrictStr | None = None
    signingServiceName: StrictStr | None = None
