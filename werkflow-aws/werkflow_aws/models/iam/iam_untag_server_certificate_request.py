from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMUntagServerCertificateRequest(BaseModel):
    ServerCertificateName: StrictStr
    TagKeys: list[StrictStr]
