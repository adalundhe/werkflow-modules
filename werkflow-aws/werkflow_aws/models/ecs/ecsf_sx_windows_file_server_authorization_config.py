from __future__ import annotations
from pydantic import BaseModel, StrictStr


class ECSFSxWindowsFileServerAuthorizationConfig(BaseModel):
    credentialsParameter: StrictStr | None = None
    domain: StrictStr | None = None
