from __future__ import annotations
from typing import Any
from pydantic import BaseModel
from .directory_service_certificate import DirectoryServiceCertificate


class DirectoryServiceDescribeCertificateResponse(BaseModel):
    Certificate: DirectoryServiceCertificate | None = None
    ResponseMetadata: dict[str, Any] | None = None
