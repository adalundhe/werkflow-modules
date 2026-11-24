from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr


class ACMExportCertificateResponse(BaseModel):
    Certificate: StrictStr | None = None
    CertificateChain: StrictStr | None = None
    PrivateKey: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
