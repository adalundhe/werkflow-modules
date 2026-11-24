from __future__ import annotations
from typing import Any
from pydantic import BaseModel, StrictStr
from .directory_service_certificate_info import DirectoryServiceCertificateInfo


class DirectoryServiceListCertificatesResponse(BaseModel):
    NextToken: StrictStr | None = None
    CertificatesInfo: list[DirectoryServiceCertificateInfo] | None = None
    ResponseMetadata: dict[str, Any] | None = None
