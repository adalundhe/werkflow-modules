from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .dms_certificate import DMSCertificate


class DMSDescribeCertificatesResponse(BaseModel):
    Marker: StrictStr | None = None
    Certificates: list[DMSCertificate] | None = None
    ResponseMetadata: dict[str, Any] | None = None
