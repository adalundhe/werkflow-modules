from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IAMUpdateServerCertificateRequest(BaseModel):
    ServerCertificateName: StrictStr
    NewPath: StrictStr | None = None
    NewServerCertificateName: StrictStr | None = None
