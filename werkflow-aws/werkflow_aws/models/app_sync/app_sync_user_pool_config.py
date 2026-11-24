from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncUserPoolConfig(BaseModel):
    userPoolId: StrictStr | None = None
    awsRegion: StrictStr | None = None
    defaultAction: StrictStr | None = None
    appIdClientRegex: StrictStr | None = None
