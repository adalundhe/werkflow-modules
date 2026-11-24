from __future__ import annotations
from pydantic import BaseModel, StrictStr


class DirectoryServiceClientCertAuthSettings(BaseModel):
    OCSPUrl: StrictStr | None = None
