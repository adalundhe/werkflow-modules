from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ConnectCreateViewVersionRequest(BaseModel):
    InstanceId: StrictStr
    ViewId: StrictStr
    VersionDescription: StrictStr | None = None
    ViewContentSha256: StrictStr | None = None
