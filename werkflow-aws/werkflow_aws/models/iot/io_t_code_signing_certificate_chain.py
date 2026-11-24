from __future__ import annotations
from pydantic import BaseModel, StrictStr


class IoTCodeSigningCertificateChain(BaseModel):
    certificateName: StrictStr | None = None
    inlineDocument: StrictStr | None = None
