from __future__ import annotations
from pydantic import BaseModel, StrictStr


class AppSyncCognitoConfig(BaseModel):
    userPoolId: StrictStr | None = None
    awsRegion: StrictStr | None = None
    appIdClientRegex: StrictStr | None = None
