from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoSyncPushSync(BaseModel):
    ApplicationArns: list[StrictStr] | None = None
    RoleArn: StrictStr | None = None
