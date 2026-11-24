from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictBool, StrictStr
from .iam_signing_certificate import IAMSigningCertificate


class IAMListSigningCertificatesResponse(BaseModel):
    Certificates: list[IAMSigningCertificate] | None = None
    IsTruncated: StrictBool | None = None
    Marker: StrictStr | None = None
    ResponseMetadata: dict[str, Any] | None = None
