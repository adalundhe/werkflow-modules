from __future__ import annotations
from pydantic import BaseModel, StrictStr


class CognitoSyncCognitoStreams(BaseModel):
    StreamName: StrictStr | None = None
    RoleArn: StrictStr | None = None
    StreamingStatus: StrictStr | None = None
