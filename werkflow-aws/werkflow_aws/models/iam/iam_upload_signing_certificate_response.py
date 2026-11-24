from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .iam_signing_certificate import IAMSigningCertificate


class IAMUploadSigningCertificateResponse(BaseModel):
    Certificate: IAMSigningCertificate | None = None
    ResponseMetadata: dict[str, Any] | None = None
