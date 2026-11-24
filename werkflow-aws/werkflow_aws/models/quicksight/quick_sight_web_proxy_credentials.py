from __future__ import annotations
from pydantic import BaseModel, StrictStr


class QuickSightWebProxyCredentials(BaseModel):
    WebProxyUsername: StrictStr
    WebProxyPassword: StrictStr
